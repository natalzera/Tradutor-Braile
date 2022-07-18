import numpy as np
from getLetters import get_img_letters

# segmentador interativo das letras em braile
class Segment_letters:
    # construtor para inicializar a imagem e os parâmetros de segmentação
    def __init__(self, img, min_percent_pixels=0.01, space_rows=10, space_columns=8, space_words=1):
        self.img = img
        self.imgs = []
        self.words_len = []

        # variáveis para a segmentação
        self.min_percent_pixels = min_percent_pixels
        self.space_words = space_words

        # variáveis sujeitas a otimização
        self.space_columns = space_columns
        self.space_rows = space_rows

    # identifica e pega as sub-imagens das letras presentes na imagem de acordo com os parâmetros de segmentação
    def _segment_letters(self):
        self.imgs, self.words_len = get_img_letters(
            self.img, self.min_percent_pixels, self.space_rows, self.space_columns, self.space_words
        )

    # retorna o quociente entre os tamanhos das sub-imagens
    def _get_quotient_sizes(self, axis=0):
        sizes = []
        for img in self.imgs:
            sizes.append(img.shape[axis])

        sizes = np.array(sizes)
        all_score = np.min(sizes) / np.max(sizes)
        min_score = np.min(sizes) / np.median(sizes)
        max_score = np.median(sizes) / np.max(sizes)
        
        # se os valores estão próximos de 1, então os tamanhos são similares
        # se os valores estão próximos de 0, então os tamanhos são bastante distintos
        return all_score, min_score, max_score


    # faz a otimização dos parâmetros da segmentação de forma interativa
    def train_parameters(self, max_interactions=10, min_score=0.7):

        for i in range(max_interactions):
            self._segment_letters()

            # obtém os scores para a otimização
            all_hor, min_hor, max_hor = self._get_quotient_sizes(1)
            all_vert, min_vert, max_vert = self._get_quotient_sizes(0)

            # se não precisa mais otimizar
            if all_vert >= min_score and all_hor >= min_score:
                break

            # para o espaço entre as linhas
            if all_vert < min_score:
                if min_vert < max_vert:
                    self.space_rows += int(3 * (1 - min_vert))
                elif self.space_rows > 1:
                    self.space_rows -= int(3 * (1 - max_vert))

            # para o espaço entre as palavras
            if all_hor < min_score:
                if min_hor < max_hor:
                    self.space_columns += int(3 * (1 - min_hor))
                elif self.space_columns > 1:
                    self.space_columns -= int(3 * (1 - max_hor))

    # aplica a segmentação da imagem retornando suas letras contidas (fazer isso depois do treino)
    def segment_image(self):
        self._segment_letters()
        return self.imgs, self.words_len

    # muda a imagem a ser segmentada sem mudar os parâmetros já treinados (a não ser que os treine novamente)
    def set_new_img(self, new_img):
        self.img = new_img