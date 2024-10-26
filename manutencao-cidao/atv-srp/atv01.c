#include <stdio.h>

typedef struct {
    char nome[50];
    float salario;
} Funcionario;

void GerenciarFuncionario(Funcionario *f, float novoSalario) {
    // Atualizar o salário do funcionário
    f->salario = novoSalario;

    // Gerar relatório
    printf("Relatório do Funcionário: %s\n", f->nome);
    printf("Salário: %.2f\n", f->salario);
}

int main() {
    Funcionario f = {"João", 5000.00};
    GerenciarFuncionario(&f, 6000.00);
    return 0;
}
