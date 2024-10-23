class Notificacao:
    def enviar(self, usuario):
        print(f'notificacao enviada ao {usuario}')

class Sistema:
    def enviar_email(self, usuario):
        notificacao = Notificacao()
        notificacao.enviar(usuario)

sistema = Sistema()
sistema.enviar_email('renan')