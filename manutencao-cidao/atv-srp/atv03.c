#include <stdio.h>

void GerenciarArquivo(char* nomeArquivo) {
    // Leitura de arquivo
    printf("Lendo o arquivo: %s\n", nomeArquivo);

    // Processamento de dados
    printf("Processando os dados do arquivo...\n");

    // Escrita no arquivo
    printf("Escrevendo no arquivo: %s\n", nomeArquivo);
}

int main() {
    GerenciarArquivo("dados.txt");
    return 0;
}
