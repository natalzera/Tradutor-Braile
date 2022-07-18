import imageio
from preProcess import pre_process
from segment import Segment_letters
from trad_letters import  *

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
    count = int(input('Número dos elementos a comparar na tradução: '))

    # pré processamento da imagem
    proc_img = pre_process(img, 127, point_size)

    # segmentação das letras
    seg = Segment_letters(proc_img, 0.01, int(2.5*point_size), int(2.3*point_size), word_space)
    seg.train_parameters(num_inter, 0.7)
    imgs, words_len = seg.segment_image()
    print('\nTamanho das palavras: ' + str(words_len)) # mostra o tamanho de cada palavra na frase total

    # leitura das letras do alfabeto como referência
    alf_letters = alfabet()

    # cálculo dos descritores de haralick das letras do alfabeto
    rel_pos = [1,1]
    desc_alf_letters = []
    for letter in alf_letters:
        co_matrix = co_occurrence_matrix(letter, rel_pos)
        desc_alf_letters.append( haralick_descriptors(co_matrix) )

    # salva a imagem processada, as imagens das letras segmentadas e as traduz
    letters = []
    imageio.imwrite('proc_img.jpg', proc_img)
    for i, letter in enumerate(imgs):
        imageio.imwrite('letters/{}.jpg'.format(i), letter)
        letters.append( traduce(letter, alf_letters, desc_alf_letters, rel_pos, count) )

    # forma a frase de acordo com as letras traduzidas e os tamanhos das palavras
    phrase = ''
    count_space = 0
    pos_space = 0
    for i in range(len(letters)):
        if count_space < len(words_len)-1 and i == words_len[count_space] + pos_space:
            phrase += ' '
            pos_space += words_len[count_space]
            count_space += 1

        phrase += letters[i]
    
    # resultado final
    print(phrase)

main()