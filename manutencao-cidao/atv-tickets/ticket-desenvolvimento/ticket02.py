class BancoDeDados:
    def verificar_usuario(self, usuario, senha):
        print(f'usuario {usuario} verificado')

class Abstracao:
    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    def autenticacao(self, usuario, senha):
        self.banco_de_dados.verificar_usuario(usuario, senha)

class Autenticacao:
    def __init__(self):
        self.abstracao = Abstracao() 

    def autenticar(self, usuario, senha):
        self.abstracao.autenticacao(usuario, senha)
    
autenticacao = Autenticacao()
autenticacao.autenticar('renan','d5YUflS56')