class BackEnd:
    def recuperar_imagens(self):
        print('imagens recuperadas')

class CarregadorImagens:
    def __init__(self, backend):
        self.backend = backend

    def carregar(self):
        return self.backend.recuperar_imagens()

backend = BackEnd()
carregador_imagens = CarregadorImagens(backend)
carregador_imagens.carregar()
