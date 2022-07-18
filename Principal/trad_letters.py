import imageio
from preProcess import *

# lê e retorna as imagens das letras do alfabeto
def alfabet():
    imgs = []

    for i in range(ord('a'), ord('z')+1):
        letter = imageio.imread('alfabeto/{}.png'.format(chr(i)))
        letter_2d = convert_gray_scale(letter)
        letter_b = linearization(letter_2d, 127)
        imgs.append(letter_b)

    return imgs

# calcula a matriz de co-ocorrência dado uma imagem e uma posição de pixel relativa
def co_occurrence_matrix(img, ref_pos):
    co_matrix = np.zeros([np.max(img)+1, np.max(img)+1])

    for x in range(1, img.shape[0]-1):
        for y in range(1, img.shape[1]-1):
            co_matrix[img[x,y], img[x+ref_pos[0], y+ref_pos[1]]] += 1

    return co_matrix / np.sum(co_matrix)

# calcula os descritores de haralick dado a matriz de co-ocorrências
def haralick_descriptors(co_matrix):
    i, j = np.ogrid[0:co_matrix.shape[0], 0:co_matrix.shape[1]]
    
    auto_correlation = (i * j * co_matrix).sum()
    contrast = (np.power((i - j), 2) * co_matrix).sum()
    dissimilarity = (np.abs(i - j) * co_matrix).sum()
    energy = np.power(co_matrix, 2).sum()
    entropy = -(co_matrix[co_matrix>0] * np.log(co_matrix[co_matrix>0])).sum()
    homogeneity = (co_matrix / (1 + np.power((i - j), 2))).sum()
    inverse_diference = (co_matrix / (1 + np.abs(i - j))).sum()
    maximum_probability = np.max(co_matrix)

    descriptors = [
        auto_correlation, contrast, dissimilarity, energy, entropy, 
        homogeneity, inverse_diference, maximum_probability
    ]
    return descriptors

# faz comparação pixel a pixel entre as imagens passadas
def pixel_difference(img1, img2):
    MSE = np.square(np.subtract(img1, img2)).mean() 
    return np.sqrt(MSE)

# calcula a distância euclidiana entre p1 e p2
def euclidean_distance(p1, p2):
    return np.sqrt( np.sum(np.square(np.array(p1) - np.array(p2))) )

# normaliza os valores do array passado para estar no intervalo [0, maxVal]
def normalize(array, maxVal):
    norm = (array - np.min(array)) / (np.max(array) - np.min(array))
    norm = norm * maxVal
    return norm

# traduz uma imagem de uma letra passada para seu char respectivo
def traduce(img_letter, alf_letters, desc_alf_letters, rel_pos, count):
    diffs = []
    distances = []

    # faz as comparações entre a imagem da letra e as do alfabeto
    for i in range(len(alf_letters)):
        # calcula a distância euclidiana entre os descritores
        co_matrix = co_occurrence_matrix(img_letter, rel_pos)
        desc = haralick_descriptors(co_matrix)
        distances.append( euclidean_distance(desc, desc_alf_letters[i]) )

        # calcula a diferença pixel a pixel
        new_img_letter, resp_letter = equal_size(img_letter, alf_letters[i])
        diffs.append(np.sum(new_img_letter - resp_letter))

    # normaliza os valore dos arrays
    distances = normalize(np.array(distances), 1)
    diffs = normalize(np.array(diffs), 1)

    # ordena ambas as listas
    scores_diffs = []
    scores_dists = []
    for i in range(len(distances)):
        scores_diffs.append((diffs[i], chr(i+ord('a'))))
        scores_dists.append((distances[i], chr(i+ord('a'))))

    scores_diffs.sort(key = lambda x: x[0], reverse=False)
    scores_dists.sort(key = lambda x: x[0], reverse=False)
    
    # usa apenas os n melhores classificados
    used_scores_diffs = scores_diffs[:count]
    used_scores_dists = scores_dists[:count]

    # retorna a 1° letra correspondente nos 2 scores
    correspondence = [el for el in used_scores_diffs if el in used_scores_dists]
    if(len(correspondence) < 1):
        return used_scores_diffs[0][1]
    else:
        return correspondence[0][1]