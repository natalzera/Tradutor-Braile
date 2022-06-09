# Tradutor de braile em imagens
## Objetivo
O projeto consiste em desenvolver um programa em linguagem **python**, com auxílio das bibliotecas **numpy**, **imageio** e outras, que receba uma imagem de input, identifica se existem escritas em braile e, se possuir, traduzi-las para caracteres alfa-numéricos.

A seguir, um exemplo do tipo de imagem que o programa irá ler e sua respectiva saída esperada:

![caneca com escritas em braile](https://storage.googleapis.com/kagglesdsdata/datasets/1885846/3084457/Braille/images/train/0000000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20220609%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220609T132118Z&X-Goog-Expires=345599&X-Goog-SignedHeaders=host&X-Goog-Signature=865ed876f3ed0b56e3921abd5536def2a7d619e60ada1c9cfa5a53d12db435235ca52dbe368c1ab6f5d9303a4d778df948c31da02532273e6a468acfd5e61ee9344c64d2906dff799a5b724c7ae626bb3bce310a7b95133a926caa22a1b42df8e6aec69945ade22c8ca9fdf9a6ce26c93e5a511821ec16922ad6b9ee94e124fcf171335c59ea51532c83b9d8a5489ddf92b7eaf068514459e18d779f1dfafcbdd69c1dc08ecc6d30093ccd2b02435cc569781c887c8e26d388fafdee8736f877ca64de76a2e359ef67eaead710484f00febbc8e7e4914cfd6648ad540381853cd8b92a3911243b4ccc5c3041fa9e61227a7615ead4f192a0e420597df42b1d95)
#### "do not touch"

## Banco de imagens
Para testar e aplicar a funcionalidade do programa, utilizou-se de um banco de imagens armazenado na comunidade [Keggle](https://www.kaggle.com/), que pode ser visto publicamente clicando [aqui](https://www.kaggle.com/datasets/changjianli/braille-dataset-for-scene-text-recognition) ou copiando o link escrito em "dataset.txt" no próprio repositório.

Visto isso, é importante notar que neste banco de imagens escolhido, devido sua principal aplicação ser para treino e teste de algoritmos de aprendizado de máquina, as pastas de Imagens e de suas respectivas Labels estão divididas em subpastas "train" e "val". Contudo, para este projeto, independemos dessa subdivisão já que não utilizaremos nenhum algoritmo de aprendizado de máquina. Portanto, podemos escolher livremente qualquer imagem do banco desde que selecionamos corretamente a label correspondente para validação das saídas do programa.

### Labels
Em particular, as labels obtidas no banco das imagens guardam muitas informações desnecessárias para o projeto. Portanto passarão por um tratamento antes de serem realmente consideradas no algoritmo.

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
Para a tradução dos caracteres em braile para algum da tabela ASCII, deve-se implementar no código a conversão de todas as letras do alfabeto:

![alfabeto em braile](https://3.bp.blogspot.com/_WzSKE_kNo6M/TJfrPiJLhkI/AAAAAAAAAHk/ETZjIgeuZnk/s1600/braille.jpg)
