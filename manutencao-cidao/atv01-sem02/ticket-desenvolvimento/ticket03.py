class BancoDeDados:
    def consultar_todos_os_dados(self):
        return 'todos os dados consultados'

class Relatorio:
    def gerar(self, banco_de_dados):
        return banco_de_dados.consultar_todos_os_dados()

banco_de_dados = BancoDeDados()
relatorio = Relatorio()
print(relatorio.gerar(banco_de_dados))