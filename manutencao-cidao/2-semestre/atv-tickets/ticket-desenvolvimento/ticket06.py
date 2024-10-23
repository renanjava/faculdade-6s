class BackEnd:
    def recuperar_imagens(self):
        print('imagens recuperadas')

class CarregadorImagens:
    def carregar(self):
        backend = BackEnd()
        return backend.recuperar_imagens()

carregadorImagens = CarregadorImagens()
carregadorImagens.carregar()