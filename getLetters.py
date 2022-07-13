import numpy as np

# retorna os limites de início e fim das linhas
def def_vertical_points(img, tolerance, j_lines):
    # variáveis base
    limits = []
    y = 0

    # intera sobre toda imagem verticalmente
    while y < img.shape[0]:
        lim = []
        # encontra a borda de cima da linha
        while y < img.shape[0] and np.count_nonzero(img[y,:]) <= tolerance * img.shape[1]:
            y += 1
        
        if y >= img.shape[0]:
            break

        lim.append(y-1)

        # encontra a borda de baixo da linha
        count = 0
        while count <= j_lines and y < img.shape[0]:
            if np.count_nonzero(img[y,:]) <= tolerance * img.shape[1]:
                count += 1
            else:
                count = 0
            y += 1

        lim.append(y-1)
        limits.append(lim)

    return limits

# retorna os limites de início e fim das letras na linha
def def_horizontal_points(img_line, tolerance, j_columns):
    # variáveis base
    limits = []
    x = 0

    # intera sobre toda linha horizontalmente
    while x < img_line.shape[1]:
        lim = []
        # encontra a borda da esquerda da letra
        while x < img_line.shape[1] and np.count_nonzero(img_line[:,x]) <= tolerance * img_line.shape[0]:
            x += 1
        
        if x >= img_line.shape[1]:
            break

        lim.append(x-1)

        # encontra a borda da direita da letra
        count = 0
        while count <= j_columns and x < img_line.shape[1]:
            if np.count_nonzero(img_line[:,x]) <= tolerance * img_line.shape[0]:
                count += 1
            else:
                count = 0
            x += 1

        lim.append(x-1)
        limits.append(lim)

    return limits

# separa, da imagem passada, todas as letras em braile presentes
def get_img_letters(img, tolerance, j_lines, j_columns, word_space):
    
    # extração das imagens das linhas
    lim_y = def_vertical_points(img, tolerance, j_lines)
    lines_img = []

    for i in range(len(lim_y)):
        lines_img.append(img[lim_y[i][0] : lim_y[i][1], :])

    # extração das imagens das letras e do tamanho das palavras
    letters_imgs = []
    words_len = []
    letter_count = 0

    for line in lines_img:
        # para cada imagem de linha, divide-a em letras
        lim_x = def_horizontal_points(line, tolerance, j_columns)

        for i in range(len(lim_x)):
            letters_imgs.append(line[:, lim_x[i][0] : lim_x[i][1]])
            
            # se possui espaço suficiente entre as letras para considerar uma nova palavra
            if i > 0 and lim_x[i][0] - lim_x[i-1][1] > j_columns * word_space:
                words_len.append(letter_count)
                letter_count = 1
            else:
                letter_count += 1

        # cada linha nova considera uma nova palavra
        words_len.append(letter_count)
        letter_count = 0

    return letters_imgs, words_len