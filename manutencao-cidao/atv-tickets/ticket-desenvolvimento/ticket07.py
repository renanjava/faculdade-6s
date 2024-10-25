class FrontEnd:
    def atualizar(self, produto):
        print(f'produto {produto} atualizado')

class Carrinho:
    def __init__(self, front_end):
        self.front_end = front_end

    def adicionar_produto(self, produto):
        return self.front_end.atualizar(produto)

front_end = FrontEnd()
carrinho = Carrinho(front_end)
carrinho.adicionar_produto('bolacha')
