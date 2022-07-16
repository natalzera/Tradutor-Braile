import numpy as np
from skimage import morphology

# converte uma imagem RGB para escala de cinza (matriz 2d)
def convert_gray_scale(img):
    if len(img) == 2:
        return img

    gray_img = img.sum(axis=2) / 3
    return gray_img.astype(np.uint8)

# retorna o complemento de uma imagem binária passada
def complement(img):
    compl_img = (img.astype(float)-1).astype(np.uint8)
    compl_img[compl_img == 255] = 1
    return compl_img

# aplica uma linearização da imagem
def linearization(img, t0):
    # otimiza t0
    while True:
        # 2 grupos da imagem e suas intensidades médias de acordo com t
        g1 = np.where(img > t0)
        g2 = np.where(img <= t0)
        
        u1 = np.mean(img[g1])
        u2 = np.mean(img[g2])
        
        t1 = (u1 + u2) / 2 # calcula o novo t
        
        # fim da otimização
        if abs(t0 - t1) < 0.5:
            t1 = int(t1)
            break
        
        t0 = t1
        
    # com o t otimizado, aplica a linearização
    ind = np.where(img > t1)
    binary = np.zeros(img.shape).astype(np.uint8)
    binary[ind] = 1
        
    return binary

# faz o pré-processamento da imagem para evidenciar os pontos desejados
def pre_process(img, threshold=127, point_size=3.4):

    # conversão para escala de cinza e binarização
    proc_img = convert_gray_scale(img)
    proc_img = linearization(proc_img, threshold)

    # inverte a imagem se necessário para a maioria dos pixels serem 0
    img_size = img.shape[0] * img.shape[1]
    if np.count_nonzero(proc_img) > img_size // 2:
        proc_img = complement(proc_img)

    # reduz as irregularidades nos pixels dos pontos identificados
    proc_img = morphology.closing(proc_img, morphology.disk(point_size*0.7)) # reduz os buracos internos
    proc_img = morphology.opening(proc_img, morphology.disk(point_size*0.7)) # reduz os vales nas bordas

    # ajusta os formatos dos pontos para ficarem mais circulares
    if point_size >= 2.5:
        proc_img = morphology.skeletonize(proc_img).astype(np.uint8)
        proc_img = morphology.dilation(proc_img, morphology.disk(point_size))

    proc_img = np.pad(proc_img, 1, 'constant') # aplica padding de 0 para auxiliar na segmentação
    proc_img[proc_img == 1] = 255
    return proc_img