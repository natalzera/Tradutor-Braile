import imageio
from skimage import morphology
from preProcess import *
from getLetters import get_img_letters

def main():
    # lê a imagem de entrada e converte para escala de cinza
    img = imageio.imread('test.jpg')
    img = convert_gray_scale(img)

    # pré-processa ela antes do algoritmo de identificação
    proc_img = limiarization(img, 127)
    proc_img = complement(proc_img)

    proc_img = morphology.closing(proc_img, morphology.disk(2))
    proc_img[proc_img == 1] = 255
    
    imageio.imwrite('proc_img.jpg', proc_img)
    
    # identifica as letras em braile e as separa em sub imagens
    imgs = get_img_letters(proc_img, 0.02, 5, 4)
    for i, img in enumerate(imgs):
        for j, letter in enumerate(img):
            imageio.imwrite('letters/'+str(i)+str(j)+'.jpg', letter)

main()