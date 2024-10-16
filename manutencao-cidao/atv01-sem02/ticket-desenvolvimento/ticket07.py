class FrontEnd:
    def atualizar(self, produto):
        print(f'produto {produto} atualizado')

class Carrinho:
    def adicionar_produto(self, produto):
        frontEnd = FrontEnd()
        return frontEnd.atualizar(produto)

carrinho = Carrinho()
carrinho.adicionar_produto('bolacha')