#include <ctype.h>
#include <stdio.h>

int get_size(const char* file_name);

int main()
{
    char nome_arquivo[100];
    FILE *arquivo;
    int esta_em_palavra = 0;
    char caractere;

    printf("Digite o nome do arquivo: ");
    scanf("%s", nome_arquivo);

    arquivo = fopen(nome_arquivo, "r");

    if (arquivo == NULL)
    {
        printf("Nao foi possivel abrir o arquivo.\n");
        return 1;
    }
    int teve_letra = 0;
    int cont_palavras = 0;
    while ((caractere = fgetc(arquivo)) != EOF)
    {
        if (isspace(caractere))
        {
            cont_palavras++;
        }
        if((caractere >= 65 && caractere <= 90) || (caractere >= 97 && caractere <= 122))
        {
            teve_letra = 1;
        }

    }
    cont_palavras = cont_palavras + teve_letra;

    if(get_size(nome_arquivo) == 0)
    {
        printf("0");
    }
    else
    {
        printf("%d\n", cont_palavras);
    }

    fclose(arquivo);

    return 0;
}

int get_size(const char* file_name)
{
    FILE *file = fopen(file_name, "r");

    if(file == NULL)
        return 0;

    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fclose(file);

    return size;
}
