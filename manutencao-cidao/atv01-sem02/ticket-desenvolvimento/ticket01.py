class Pagamento:
    def efetuar_pagamento(self, number):
        print (f'pagou {number}')

class CarrinhoDeCompras:
    def processar_pagamento(self):
        pagamento = Pagamento()
        pagamento.efetuar_pagamento(self.total())

    def total(self):
        return 500

carrinho = CarrinhoDeCompras()
carrinho.processar_pagamento()