import numpy as np

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

# dependendo de gamma, pode evidenciar os pixels claros (gamma > 1) ou os escuros (0 < gamma < 1)
def gamma_adj(img, gamma=2.5):
    newImg = 255 * np.power(img.astype(np.int32) / 255, gamma)
    newImg = newImg.astype(np.uint8)
    return newImg

# faz uma função em sigmoide, evidenciando os pixels de valor intermediário (contraste)
def logistic_func(img, k=0.06):
    newImg = 255 / (1 + np.exp(-k * (img.astype(np.int32) - 127)))
    newImg = newImg.astype(np.uint8)
    return newImg

# aplica uma linearização da imagem
def limiarization(img, t0):
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