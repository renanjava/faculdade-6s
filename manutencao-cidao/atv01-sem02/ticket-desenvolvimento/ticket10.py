class Cliente:
    def __init__(self):
        print('oi')

class Status:
    def __init__(self):
        self.status = 'iniciado'
    def alterar(self, status):
        self.status = status

class Pedido:
    cliente = Cliente()
    status = Status()
    def alterar_status(self, status):
        print(self.status.status)
        self.status.alterar(status)
        print(self.status.status)


pedido = Pedido()
pedido.alterar_status('finalizado')

