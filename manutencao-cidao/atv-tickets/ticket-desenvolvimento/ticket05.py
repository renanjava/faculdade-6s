class Usuario:
    def __init__(self):
        self.inativo = False

    def monitorar_sessao(self):
        if self.verificar_inatividade():
            self.logout()

    def verificar_inatividade(self):
        return self.inativo

    def logout(self):
        print('usuário desconectado')

usuario = Usuario()
usuario.inativo = True
usuario.monitorar_sessao()
