# Tradutor de braile em imagens
## Objetivo
O projeto consiste em desenvolver um programa em linguagem **python**, com auxílio das bibliotecas **numpy**, **imageio** e **skimage** que recebe uma imagem contendo escritas em braile e consegue escrever em um arquivo de texto sua respectiva tradução.

A seguir, um exemplo do tipo de imagem que o programa irá ler e sua respectiva saída esperada:

![caneca com escritas em braile](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/test.jpg)
#### "do not touch"

## Banco de imagens
Para testar e aplicar a funcionalidade do programa, utilizou-se de imagens contidas em um banco armazenado na comunidade [Keggle](https://www.kaggle.com/), que pode ser visto publicamente clicando [aqui](https://www.kaggle.com/datasets/changjianli/braille-dataset-for-scene-text-recognition) ou copiando o link escrito em "link.txt" na pasta "dataset".

Sobre este banco de imagens, é importante notar que, por ser destinado ao treino e teste de redes neurais, as pastas das imagens e labels estão divididas em subpastas "train" e "val", mas não será levado em conta essa divisão para este programa. Além disso, é necessário uma verificação da legibilibilidade para a tradução antes de realmete fazê-la, uma vez que algumas imagens do banco estão muito poluídas de outros elementos, o que impossibilita a tradução sem usar do auxílio de uma rede neural. Portanto, as imagens que podem ser utilizadas no programa devem ser realmente selecionadas manualmente deste banco.

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
accessible entrance
```

Utilizando do **labels.py** (na pasta "dataset" do projeto), fazemos a tradução das labels e podemos utilizá-las para debug do código. Mas vale lembrar que este não é o foco do projeto, é apenas uma automação de um processo secundário em nosso programa (poderíamos muito bem fazer a tradução manualmente ou na internet).

## Algoritmo

### Parte 1: Pré-processamento
Primeiramente, o código irá receber como input a imagem selecionada e **pré-processá-la** (convertendo para escala de cinza, binarizando-a e aplicando morfologia para evidenciar os círculos), dessa forma teremos nela apenas as escritas em braile evidentes na imagem.

A seguir, um exemplo de imagem de input após o pré-processamento:

![escritas em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/proc_img.jpg)

### Parte 2: Extração das letras em braile
Após a imagem ser pré-processada, o algoritmo aplicará uma função que irá separa-la em sub-imagens ordenadamente, em que cada uma guarda uma letra em braile escrita na imagem total. Essa separação é feita considerando as distâncias entre os pontos presentes na imagem, agrupando os mais próximos e separando como letras diferentes os mais distantes.

A seguir, as letras extraídas da imagem processada:

![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/00.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/01.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/10.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/11.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/12.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/20.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/21.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/22.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/23.jpg)
![letra em braile em preto e branco](https://github.com/natalzera/Tradutor-Braile/blob/main/Parcial/letters/24.jpg)

Além disso, considerando as distâncias entre as letras na imagem, esta mesma função calcula e retorna a quantidade de letras que cada palavra vai possuir (em ordem).

A seguir, o vetor de tamanho das palavras calculado no exemplo acima:
```Python3
[2, 3, 5]
```

### Parte 3: Tradução das palavras

Dado as imagens de cada letra retiradas da imagem de entrada, iremos comparar cada uma com as imagens de referência para todas as 26 letras do alfabeto (do 2° banco de imagens utilizado) utilizando comparação por **textura**.

A seguir, um exemplo das imagens e labels dadas ao algoritmo para a tradução:

![alfabeto em braile](https://3.bp.blogspot.com/_WzSKE_kNo6M/TJfrPiJLhkI/AAAAAAAAAHk/ETZjIgeuZnk/s1600/braille.jpg)

Após a comparação e definição de quais imagens de referência ela se aprixima mais, podemos traduzir a letra em braile da imagem para um caractere do alfabeto. Fazendo esse processo com todas as imagens das letras retirada da imagem de entrada e concatenando as saídas, obtemos a saída final do programa:

#### "do not touch"

Além disso, é possível debugar o programa utilizando uma função de comparação da saída dele com a label referente à imagem do 1° banco.
