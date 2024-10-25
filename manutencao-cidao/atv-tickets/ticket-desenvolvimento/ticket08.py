class Notificacao:
    def enviar(self, usuario):
        print(f'notificação enviada ao {usuario}')

class Sistema:
    def __init__(self, notificacao):
        self.notificacao = notificacao

    def enviar_email(self, usuario):
        self.notificacao.enviar(usuario)

notificacao = Notificacao()
sistema = Sistema(notificacao)
sistema.enviar_email('renan')
