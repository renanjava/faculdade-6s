#include <stdio.h>

typedef struct {
    int id;
    float valor;
} Pedido;

void ProcessarPedido(Pedido *pedido) {
    // Processa o pedido
    printf("Processando pedido #%d de valor %.2f\n", pedido->id, pedido->valor);

    // Enviar notificação ao cliente
    printf("Enviando notificação para o cliente do pedido #%d\n", pedido->id);
}

int main() {
    Pedido p = {1, 100.00};
    ProcessarPedido(&p);
    return 0;
}
