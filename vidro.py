from tkinter import *
from tkinter import ttk
from conexao_vidro import ConexaoVidro
import sys

class Vidro:

    def __init__(self):
        self.cadastro_vidro = None

        self.id_vidro = None
        self.codigo_vidro = None
        self.descricao_vidro = None
        self.preco_vidro = None
        self.lb_codigo_vidro = None
        self.lb_descricao_vidro = None
        self.lb_preco_vidro = None
        self.bt_salvar_vidro = None
        self.bt_cancelar_vidro = None
        self.entry_codigo_vidro = None
        self.entry_descricao_vidro = None
        self.entry_preco_vidro = None
        
        self.conexao = ConexaoVidro()

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


    def chama_tela_cadastro_vidro(self):
        # Instancia de Tk()
        self.cadastro_vidro = Tk()
        
        # Confgurações da tela
        self.cadastro_vidro.title("Cadastro de Vidros")
        self.cadastro_vidro.geometry("300x300")
        self.centraliza_janela(self.cadastro_vidro)
        
        # Componentes da tela
        self.entry_codigo_vidro = Entry(self.cadastro_vidro)
        self.entry_descricao_vidro = Entry(self.cadastro_vidro)
        self.entry_preco_vidro = Entry(self.cadastro_vidro)
        
        self.lb_codigo_vidro = Label(self.cadastro_vidro, text="Código")
        self.lb_codigo_vidro.grid(row=0, column=0, padx=20, pady=20)
        self.entry_codigo_vidro.grid(row=0, column=1, padx=20, pady=20)
        
        self.lb_descricao_vidro = Label(self.cadastro_vidro, text="Descrição")
        self.lb_descricao_vidro.grid(row=1, column=0, padx=20, pady=20)
        self.entry_descricao_vidro.grid(row=1, column=1, padx=20, pady=20)
        
        self.lb_preco_vidro = Label(self.cadastro_vidro, text="Preço por m²")
        self.lb_preco_vidro.grid(row=2, column=0, padx=20, pady=20)
        self.entry_preco_vidro.grid(row=2, column=1, padx=20, pady=20)
        
        self.bt_salvar_vidro = Button(self.cadastro_vidro, text="Salvar", command=self.event_bt_salvar)
        self.bt_salvar_vidro.grid(row=4, column=0, padx=20, pady=20, sticky=E)
        
        self.bt_cancelar_vidro = Button(self.cadastro_vidro, text="Cancelar", command=self.event_bt_cancelar)
        self.bt_cancelar_vidro.grid(row=4, column=1, padx=20, pady=20, sticky=E)   
        
        return self.cadastro_vidro.mainloop()
 
    
    def event_bt_cancelar(self):
        self.cadastro_vidro.destroy()
        
    
    def event_bt_salvar(self):
        codigo = self.entry_codigo_vidro.get()
        descricao = self.entry_descricao_vidro.get()
        preco = self.entry_preco_vidro.get()
        
        """
        CRIAR UMA FUNCAO QUE TROQUE A VIRGULA POR PONTO, PRINCIPALMENTE NO CAMPO PRECO
        """ 
        
        self.conexao.inserted_values = (codigo, descricao, preco)
        
        self.conexao.insert_vidro()

