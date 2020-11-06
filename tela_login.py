from tkinter import *
from tkinter import messagebox
from novo_usuario import NovoUsuario
import sys
from conexao_usuario import ConexaoUsuario
from tela_principal import TelaPrincipal


class Login:
    def __init__(self):
        self.tela_login = Tk()
        self.novo_usuario = None
        self.lb_usuario = None
        self.lb_senha = None
        self.entry_usuario = Entry(self.tela_login)
        self.entry_senha = Entry(self.tela_login, show="*")
        self.bt_cadastrar = None
        self.bt_login = None
        self.bt_cancelar = None
        self.lb_space = None

        """
            Para uso do banco de dados
        """
        self.conexao = ConexaoUsuario()
        


    def centraliza_janela(self, instancia_tk):
        """
        Metodo para centralizar a tela
        """
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)

        posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 2) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


    @staticmethod  # metodo estático(metodo da classe)
    def event_bt_cancelar():
        sys.exit()

   
    def event_bt_cadastrar(self):
        """
        Chama a tela para cadastrar novos usuarios
        """
        self.novo_usuario = NovoUsuario().chama_tela_novo_usuario()

    
    def event_bt_login(self):
        """
        METODO QUE VERIFICA NO BANCO DE DADOS O NOME DO USUARIO E A SENHA
        BOTÃO LOGIN
        """
        busca_usuario = self.conexao.buscar_user()
        usuario_senha = (self.entry_usuario.get(), self.entry_senha.get())

        for resultado in busca_usuario:

            if resultado == usuario_senha:
                messagebox.showinfo("Bem vindo", "Seja Bem vindo " + self.entry_usuario.get().title())
                TelaPrincipal().chama_tela_principal()

                """
                ENCONTRAR UMA FORMA DE FECHAR A JANELA DE LOGIN APÓS O USUARIO LOGAR COM SUCESSO
                """

            if usuario_senha not in busca_usuario:
                messagebox.showinfo("Atenção", "Usuario não cadastrado")
                break


    def chama_tela_login(self):
        self.tela_login.title("Login")
        self.tela_login.geometry("250x160")
        self.centraliza_janela(self.tela_login)
        self.lb_usuario = Label(self.tela_login, text="Usuario:")
        self.lb_usuario.grid(row=0, column=0, pady=20, padx=20)
        self.entry_usuario.grid(row=0, column=1)
        self.lb_senha = Label(self.tela_login, text="Senha:")
        self.lb_senha.grid(row=1, column=0)
        self.entry_senha.grid(row=1, column=1)
        self.lb_space = Label(self.tela_login, text="")
        self.lb_space.grid(row=0, column=2)

        # Botões
        self.bt_cadastrar = Button(self.tela_login, text="Cadastrar", command=self.event_bt_cadastrar)
        self.bt_cadastrar.grid(row=2, column=0, pady=20)
        self.bt_login = Button(self.tela_login, text="Login", command=self.event_bt_login)
        self.bt_login.grid(row=2, column=1, pady=20, sticky=W)
        self.bt_cancelar = Button(self.tela_login, text="Cancelar", command=self.event_bt_cancelar)
        self.bt_cancelar.grid(row=2, column=1, pady=20, sticky=E)

        return self.tela_login.mainloop()


#chama = Login().chama_tela_login()