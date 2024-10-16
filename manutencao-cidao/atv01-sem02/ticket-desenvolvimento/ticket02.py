class BancoDeDados:
    def verificar_usuario(self, usuario, senha):
        print(f'usuario {usuario} verificado')


class Autenticacao:
    def autenticar(self, usuario, senha, banco_de_dados):
        banco_de_dados.verificar_usuario(usuario, senha)

    
banco_de_dados = BancoDeDados()
autenticacao = Autenticacao()
autenticacao.autenticar('renan','d5YUflS56', banco_de_dados)