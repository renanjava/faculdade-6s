class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def atualizar(self, rua, numero):
        self.rua = rua
        self.numero = numero
        print('realizando mudanças...')

class Usuario:
    def __init__(self, nome, idade, rua, numero):
        self.nome = nome
        self.idade = idade
        self.endereco = Endereco(rua, numero)

class BancoDeDados:
    def __init__(self):
        self.usuario = Usuario('renan', 20, 'rua1', 'numero1')

class Perfil:
    def atualizar_perfil(self, dados, banco_de_dados):
        endereco_atual = banco_de_dados.usuario.endereco
        print(endereco_atual.rua)
        print(endereco_atual.numero)
        
        endereco_atual.atualizar(dados['endereco']['rua'], dados['endereco']['numero'])
        
        print(endereco_atual.rua)
        print(endereco_atual.numero)

banco_de_dados = BancoDeDados()
perfil = Perfil()
dicionario = {
    'endereco': {
        'rua': 'nova_rua',
        'numero': 'novo_numero'
    }
}
perfil.atualizar_perfil(dicionario, banco_de_dados)
