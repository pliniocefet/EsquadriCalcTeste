from tkinter import *
from conexao_usuario import ConexaoUsuario
from tkinter import messagebox

class NovoUsuario:
    
    def __init__(self):
        self.tela_novo_usuario = Tk()
        self.lb_nome_usuario = None
        self.lb_senha_usuario = None
        self.entry_nome_usuario = Entry(self.tela_novo_usuario)
        self.entry_senha_usuario = Entry(self.tela_novo_usuario, show="*")
        self.bt_cadatrar_novo_usuario = None
        
        """
            Para uso do banco de dados
        """
        self.conexao = ConexaoUsuario()
        
        
    """
    Metodo para centralizar a tela    
    """
    def centraliza_janela(self, instancia_tk):    
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)
        
        posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 2) - (altura_janela))
                      
        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))
        
        
    def chama_tela_novo_usuario(self):
        """
        CHAMA A TELA DE CADASTRO DE NOVOS USUÁRIOS
        """
        self.tela_novo_usuario.title("Novo Usuário")
        self.tela_novo_usuario.geometry("300x150")
        self.centraliza_janela(self.tela_novo_usuario)
        
        self.lb_nome_usuario = Label(self.tela_novo_usuario, text="Nome de Usuario:")
        self.lb_nome_usuario.grid(row=0, column=0, padx=20, pady=20)
        
        self.entry_nome_usuario.grid(row=0, column=1, padx=20, pady=20)
        
        self.lb_senha_usuario = Label(self.tela_novo_usuario, text="Senha:")
        self.lb_senha_usuario.grid(row=1, column=0)
     
        self.entry_senha_usuario.grid(row=1, column=1)
        
        self.bt_cadatrar_novo_usuario = Button(self.tela_novo_usuario, text="Salvar", command=self.event_bt_salvar)
        
        self.bt_cadatrar_novo_usuario.place(x=150, y=100)
        
        
        return self.tela_novo_usuario.mainloop()
    
    
    def event_bt_salvar(self):
        self.conexao.inserted_values = (self.entry_nome_usuario.get().lower(), self.entry_senha_usuario.get().lower())
        
        """
        ENCONTRAR UMA FORMA DE O USUARIO NÃO CADASTRAR UM LOGIN EM BRANCO
        E TAMBÉM NÃO CADASTRAR USUARIOS COM O MESMO NOME
        """
                
        self.conexao.insert_user()
        
        self.tela_novo_usuario.destroy()
        
        