class BancoDeDados:
    def consultar_compras(self, usuario):
        return f'historico de {usuario}'

class HistoricoCompras:
    def carregar_historico(self, usuario):
        banco_de_dados = BancoDeDados()
        return banco_de_dados.consultar_compras(usuario)

historico_compras = HistoricoCompras()
print(historico_compras.carregar_historico('renan'))