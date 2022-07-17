# faz o tratamento das informações das labels do primeiro arquivo e passa para o outro
def get_labels(file_name_in, file_name_out):
    # abertura do arquivo e leitura do número de palavras
    file_in = open(file_name_in)
    num_words = int(file_in.readline().strip())
    all_words = ''

    # leitura concatenação das palavras no final da linha
    for i in range(num_words):
        line = file_in.readline().strip()
        word = line.split(',')[-1]
        word = word.replace('"', '')

        if all_words != '': all_words += ' '
        all_words += word

    file_in.close()

    # abertura e escrita no novo arquivo a palavra total
    file_out = open(file_name_out, 'w')
    file_out.write(all_words)
    file_out.close()

def main():
    labels_path = 'used_labels/' # pasta das labels utilizadas do banco de imagens
    imgs_path = 'selected_imgs/' # pasta das imagens selecionadas com as labels tratadas

    # leitura do arquivo de informações para a geração dos demais
    file_info = open('origens.txt')
    line = file_info.readline()

    while line != '':
        # leitura do nome dos arquivos de labels relacionados
        line = file_info.readline().strip()
        if line == '': break
        files_names = line.replace('.jpg', '.txt').split('     - ')
        
        # tratamento das labels e escrita no arquivo de saída
        if files_names[1] != 'na internet':
            get_labels(labels_path + files_names[1], imgs_path + files_names[0])

    file_info.close()

main()