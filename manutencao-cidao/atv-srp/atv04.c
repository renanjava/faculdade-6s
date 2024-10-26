#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    char email[50];
} Usuario;

void CadastrarUsuario(Usuario *u) {
    // Cadastro de usuário
    printf("Cadastrando usuário: %s\n", u->nome);
    // Validação do e-mail
    if (strchr(u->email, '@') == NULL) {
        printf("Email inválido!\n");
    } else {
        printf("Email válido.\n");
    }
}
int main() {
    Usuario u = {"Maria", "maria.exemplo.com"};
    CadastrarUsuario(&u);
    return 0;
}
