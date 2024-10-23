class Usuario:
    def monitorar_sessao(self):
        inativo = True
        if inativo:
            self.logout()

    def logout(self):
        print('usuario desconectado')

usuario = Usuario()
usuario.monitorar_sessao()