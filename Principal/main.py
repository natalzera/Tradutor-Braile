import imageio
from preProcess import pre_process
from segment import Segment_letters

def main():
    # leitura dos parâmetros
    filename = str(input('Diretório da imagem: '))
    try:
        img = imageio.imread(filename)
    except:
        print('Não foi possível abrir a imagem')
        return

    point_size = float(input('Tamanho estimado dos pontos: '))
    word_space = float(input('Distância entre as palavras (em n° de pontos): '))
    num_inter = int(input('Número máximo de interações: '))

    # pré processamento da imagem
    proc_img = pre_process(img, 127, point_size)

    # segmentação das letras
    seg = Segment_letters(proc_img, 0.01, int(2.5*point_size), int(2.3*point_size), word_space)
    seg.train_parameters(num_inter, 0.7)
    imgs, words_len = seg.segment_image()

    # salva a imagem processada e as imagens das letras segmentadas
    print(words_len) # mostra os tamanhos das palavras identificadas na imagem (em ordem)
    imageio.imwrite('proc_img.jpg', proc_img)
    for i, letter in enumerate(imgs):
        imageio.imwrite('letters/{}.jpg'.format(i), letter)

main()