class Cliente:
    def __init__(self, nome):
        self.nome = nome
        print(f'Cliente {self.nome} criado.')

class Status:
    def __init__(self):
        self.estado = 'iniciado'

    def alterar(self, novo_estado):
        self.estado = novo_estado

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.status = Status()

    def alterar_status(self, novo_estado):
        print(f'Status atual: {self.status.estado}')
        self.status.alterar(novo_estado)
        print(f'Status alterado para: {self.status.estado}')

cliente = Cliente('Renan')
pedido = Pedido(cliente)
pedido.alterar_status('finalizado')
