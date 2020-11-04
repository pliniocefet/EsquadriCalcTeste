from tkinter import *
from tkinter import messagebox
from conexao_usuario import ConexaoUsuario

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