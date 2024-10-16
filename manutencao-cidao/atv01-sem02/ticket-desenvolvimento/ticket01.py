import abc

class IPagamento(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def efetuar_pagamento(self, number):
        return

class Pagamento(IPagamento):
    def efetuar_pagamento(self, number):
        print (f'pagou {number}')

class CarrinhoDeCompras:
    def processar_pagamento(self, pagamento: IPagamento):
        pagamento.efetuar_pagamento(self.total())

    def total(self):
        return 500

carrinho = CarrinhoDeCompras()
pagamento = Pagamento()
carrinho.processar_pagamento(pagamento)