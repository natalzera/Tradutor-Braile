import numpy as np

# retorna os limites de início e fim das linhas
def def_vertical_points(img, tolerance, j_lines):
    # variáveis base
    limits = []
    y = 0

    # intera sobre toda imagem verticalmente
    while y < img.shape[0]:
        lim = []

        # encontra a parte de cima da linha
        while y < img.shape[0] and np.count_nonzero(img[y,:]) <= tolerance * img.shape[1]:
            y += 1
        
        if y >= img.shape[0]:
            break

        lim.append(y-1)

        # encontra a parte de baixo da linha
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

    # intera sobre toda imagem verticalmente
    while x < img_line.shape[1]:
        lim = []

        # encontra a parte de cima da linha
        while x < img_line.shape[1] and np.count_nonzero(img_line[:,x]) <= tolerance * img_line.shape[0]:
            x += 1
        
        if x >= img_line.shape[1]:
            break

        lim.append(x-1)

        # encontra a parte de baixo da linha
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

# separa da imagem passada, todas as letras em braile presentes
def get_img_letters(img, tolerance, j_lines, j_columns):
    
    # extração das imagens das linhas
    lim_y = def_vertical_points(img, tolerance, j_lines)
    lines_img = []

    for i in range(len(lim_y)):
        lines_img.append(img[lim_y[i][0] : lim_y[i][1], :])

    # extração das imagens das letras
    letters_imgs = []
    for line in lines_img:
        # para cada imagem de linha
        lim_x = def_horizontal_points(line, tolerance, j_columns)
        letters_line = []

        for i in range(len(lim_x)):
            letters_line.append(line[:, lim_x[i][0] : lim_x[i][1]])
        
        letters_imgs.append(letters_line)

    return letters_imgs