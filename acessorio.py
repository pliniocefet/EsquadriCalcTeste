from tkinter import *
from tkinter import ttk
from conexao_acessorio import ConexaoAcessorio
import sys

class Acessorio:

    def __init__(self):
        self.cadastro_acessorio = None

        self.id_acessorio = None
        self.codigo_acessorio = None
        self.descricao_acessorio = None
        self.preco_acessorio = None
        self.linha_acessorio = None
        self.lb_codigo_acessorio = None
        self.lb_descricao_acessorio = None
        self.lb_preco_acessorio = None
        self.lb_linha_acessorio = None
        self.bt_salvar_acessorio = None
        self.bt_cancelar_acessorio = None
        self.entry_codigo_acessorio = None
        self.entry_descricao_acessorio = None
        self.entry_preco_acessorio = None
        self.combobox_linha_acessorio = None
        
        self.conexao = ConexaoAcessorio()

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


    def chama_tela_cadastro_acessorio(self):
        # Instancia de Tk()
        self.cadastro_acessorio = Tk()
        
        # Confgurações da tela
        self.cadastro_acessorio.title("Cadastro de Acessorios")
        self.cadastro_acessorio.geometry("300x300")
        self.centraliza_janela(self.cadastro_acessorio)
        
        # Componentes da tela
        self.entry_codigo_acessorio = Entry(self.cadastro_acessorio)
        self.entry_descricao_acessorio = Entry(self.cadastro_acessorio)
        self.entry_preco_acessorio = Entry(self.cadastro_acessorio)
        
        # Combobox linhas de perfis
        self.combobox_linha_acessorio = ttk.Combobox(self.cadastro_acessorio, width=18)
        self.combobox_linha_acessorio["values"] = ("Linha Suprema", "Linha Gold", "Linha Convencional", "Linha 25", "Linha 30")
        
        self.lb_codigo_acessorio = Label(self.cadastro_acessorio, text="Código")
        self.lb_codigo_acessorio.grid(row=0, column=0, padx=20, pady=20)
        self.entry_codigo_acessorio.grid(row=0, column=1, padx=20, pady=20)
        
        self.lb_descricao_acessorio = Label(self.cadastro_acessorio, text="Descrição")
        self.lb_descricao_acessorio.grid(row=1, column=0, padx=20, pady=20)
        self.entry_descricao_acessorio.grid(row=1, column=1, padx=20, pady=20)
        
        self.lb_preco_acessorio = Label(self.cadastro_acessorio, text="Preço unitário")
        self.lb_preco_acessorio.grid(row=2, column=0, padx=20, pady=20)
        self.entry_preco_acessorio.grid(row=2, column=1, padx=20, pady=20)
        
        self.lb_linha_acessorio = Label(self.cadastro_acessorio, text="Linha")
        self.lb_linha_acessorio.grid(row=3, column=0, padx=20, pady=20)
        self.combobox_linha_acessorio.grid(row=3, column=1, padx=20, pady=20)
        
        self.bt_salvar_acessorio = Button(self.cadastro_acessorio, text="Salvar", command=self.event_bt_salvar)
        self.bt_salvar_acessorio.grid(row=4, column=0, padx=20, pady=20, sticky=E)
        
        self.bt_cancelar_acessorio = Button(self.cadastro_acessorio, text="Cancelar", command=self.event_bt_cancelar)
        self.bt_cancelar_acessorio.grid(row=4, column=1, padx=20, pady=20, sticky=E)   
        
        return self.cadastro_acessorio.mainloop()
 
    
    def event_bt_cancelar(self):
        self.cadastro_acessorio.destroy()
        
    
    def event_bt_salvar(self):
        codigo = self.entry_codigo_acessorio.get()
        descricao = self.entry_descricao_acessorio.get()
        preco = self.entry_preco_acessorio.get()
        linha = self.combobox_linha_acessorio.get()
        
        """
        CRIAR UMA FUNCAO QUE TROQUE A VIRGULA POR PONTO, PRINCIPALMENTE NO CAMPO PREÇO
        """ 
        
        self.conexao.inserted_values = (codigo, descricao, preco, linha)
        
        self.conexao.insert_acessorio()

