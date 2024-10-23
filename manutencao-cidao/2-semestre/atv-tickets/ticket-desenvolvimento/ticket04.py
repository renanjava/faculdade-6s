class Endereco:
    def atualizar(self, dados, usuario):
        usuario.rua = dados['rua']
        usuario.numero = dados['numero']
        print('realizando mudanças...')

class Usuario:
    endereco = Endereco()

    def __init__(self, nome, idade, rua, numero):
        self.nome = nome
        self.idade = idade
        self.endereco.rua = rua
        self.endereco.numero = numero

class BancoDeDados:
    usuario = Usuario('renan', 20, 'rua1', 'numero1')

class Perfil:
    def atualizar_perfil(self, dados, banco_de_dados):
        print(banco_de_dados.usuario.endereco.rua)
        print(banco_de_dados.usuario.endereco.numero)
        banco_de_dados.usuario.endereco.atualizar(dados['endereco'], banco_de_dados.usuario.endereco)
        print(banco_de_dados.usuario.endereco.rua)
        print(banco_de_dados.usuario.endereco.numero)

banco_de_dados = BancoDeDados()
perfil = Perfil()
dicionario = {
    'endereco': {
        'rua': 'nova_rua',
        'numero': 'novo_numero'
    }
}
perfil.atualizar_perfil(dicionario, banco_de_dados)



