# Tradutor de braile em imagens
## Objetivo
O projeto consiste em desenvolver um programa em linguagem **python**, com auxílio das bibliotecas **numpy**, **imageio**, **skimage** etc, que receba uma imagem de input, identifica se existem escritas em braile e, se possuir, traduzi-las para caracteres alfa-numéricos.

A seguir, um exemplo do tipo de imagem que o programa irá ler e sua respectiva saída esperada:

![caneca com escritas em braile](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/test.jpg)
#### "do not touch"

## Banco de imagens
Para testar e aplicar a funcionalidade do programa, utilizou-se de um banco de imagens armazenado na comunidade [Keggle](https://www.kaggle.com/), que pode ser visto publicamente clicando [aqui](https://www.kaggle.com/datasets/changjianli/braille-dataset-for-scene-text-recognition) ou copiando o primeiro link escrito em "dataset.txt" no próprio repositório.

Sobre este banco de imagens, é importante notar que, por ser destinado ao treino e teste de redes neurais, as pastas das imagens e labels estão divididas em subpastas "train" e "val", mas não será levado em conta essa divisão para este programa. Além disso, é necessário uma verificação da legibilibilidade para a tradução antes de realmete fazê-la, uma vez que algumas imagens passadas estão muito poluídas de outros elementos do cenário, o que impossibilita a tradução sem usar do auxílio de uma rede neural.

Outro banco de imagens utilizado para o algoritmo identificar as letras, também obtido no Keggle, pode ser acessado publicamente [aqui](https://www.kaggle.com/datasets/adviksharma/braille-images-for-english-characters) ou copiando o segundo link escrito em "dataset.txt" no próprio repositório. As imagens de cada letra obtidas nele poderão ser tratadas para se comparar com as letras extraídas de imagens do primeiro banco.

### Labels
Em particular, as labels obtidas no primeiro banco das imagens guardam muitas informações desnecessárias para o projeto. Portanto passarão por um tratamento antes de serem realmente consideradas no algoritmo.

A seguir, um exemplo de label disponível no dataset:
```
2
187,468,217,470,248,473,279,475,309,478,340,480,371,483,369,513,338,510,308,508,278,505,247,503,217,500,187,498,"accessible"
387,483,414,485,441,487,469,489,496,491,523,493,551,495,549,526,522,524,495,522,468,520,441,518,414,516,387,514,"entrance"
```
Deverá ser tratada para:
```
"accessible entrance"
```

## Algoritmo

### Parte 1: Extração das letras em braile
Primeiramente, o código irá receber como input alguma imagem selecionada do 1° banco de imagens (ou qualquer outra desejada pelo usuário) e **pré-processá-la** (convertendo para escala de cinza, aplicando filtro de luminosidade e binarizando-a), dessa forma teremos nela apenas as escritas em braile evidentes na imagem.

A seguir, um exemplo de imagem de input após o pré-processamento:

![escritas em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/proc_img.jpg)

Após a imagem ser pré-processada, o algoritmo aplicará uma função que irá separa-la em sub-imagens ordenadamente, em que cada uma guarda uma letra em braile escrita na imagem total.

A seguir, um exemplo das letras extraídas da imagem processada:

![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/00.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/01.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/10.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/11.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/12.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/13.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/20.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/21.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/22.jpg)

### Parte 2: Tradução das letras
![alfabeto em braile](https://3.bp.blogspot.com/_WzSKE_kNo6M/TJfrPiJLhkI/AAAAAAAAAHk/ETZjIgeuZnk/s1600/braille.jpg)
