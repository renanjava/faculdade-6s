class BancoDeDados:
    def consultar_compras(self, usuario):
        return f'historico de {usuario}'

class HistoricoCompras:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def carregar_historico(self, usuario):
        return self.banco_de_dados.consultar_compras(usuario)

banco_de_dados = BancoDeDados()
historico_compras = HistoricoCompras(banco_de_dados)
print(historico_compras.carregar_historico('renan'))