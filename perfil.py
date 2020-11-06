from tkinter import *
from tkinter import ttk
from conexao_perfil import ConexaoPerfil
import sys

class Perfil:

    def __init__(self):
        self.cadastro_perfil = None

        self.id_perfil = None
        self.codigo_perfil = None
        self.descricao_perfil = None
        self.kg_por_metro_perfil = None
        self.linha_perfil = None
        self.lb_codigo_perfil = None
        self.lb_descricao_perfil = None
        self.lb_kg_metro_perfil = None
        self.lb_linha_perfil = None
        self.bt_salvar_perfil = None
        self.bt_cancelar_perfil = None
        self.entry_codigo_perfil = None
        self.entry_descricao_perfil = None
        self.entry_kg_metro_perfil = None
        self.combobox_linha_perfil = None
        self.lb_comprimento_perfil = None
        
        self.conexao = ConexaoPerfil()

    
    def centraliza_janela(self, instancia_tk):
        """
        Metodo para centralizar a tela
        """
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)

        posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 3) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


    def chama_tela_cadastro_perfil(self):
        # Instancia de Tk()
        self.cadastro_perfil = Tk()
        
        # Confgurações da tela
        self.cadastro_perfil.title("Cadastro de Perfis")
        self.cadastro_perfil.geometry("300x400")
        self.centraliza_janela(self.cadastro_perfil)
        
        # Componentes da tela
        self.entry_codigo_perfil = Entry(self.cadastro_perfil)
        self.entry_descricao_perfil = Entry(self.cadastro_perfil)
        self.entry_kg_metro_perfil = Entry(self.cadastro_perfil)
        self.entry_comprimento_perfil = Entry(self.cadastro_perfil)
        
        # Combobox linhas de perfis
        self.combobox_linha_perfil = ttk.Combobox(self.cadastro_perfil, width=18)
        self.combobox_linha_perfil["values"] = ("Linha Suprema", "Linha Gold", "Linha Convencional", "Linha 25", "Linha 30")
        
        self.lb_codigo_perfil = Label(self.cadastro_perfil, text="Código")
        self.lb_codigo_perfil.grid(row=0, column=0, padx=20, pady=20)
        self.entry_codigo_perfil.grid(row=0, column=1, padx=20, pady=20)
        
        self.lb_descricao_perfil = Label(self.cadastro_perfil, text="Descrição")
        self.lb_descricao_perfil.grid(row=1, column=0, padx=20, pady=20)
        self.entry_descricao_perfil.grid(row=1, column=1, padx=20, pady=20)
        
        self.lb_kg_metro_perfil = Label(self.cadastro_perfil, text="Kg/m")
        self.lb_kg_metro_perfil.grid(row=2, column=0, padx=20, pady=20)
        self.entry_kg_metro_perfil.grid(row=2, column=1, padx=20, pady=20)
        
        self.lb_linha_perfil = Label(self.cadastro_perfil, text="Linha")
        self.lb_linha_perfil.grid(row=3, column=0, padx=20, pady=20)
        self.combobox_linha_perfil.grid(row=3, column=1, padx=20, pady=20)
        
        self.lb_comprimento_perfil = Label(self.cadastro_perfil, text="Comprimento:")
        self.lb_comprimento_perfil.grid(row=4, column=0, padx=20, pady=20)
        self.entry_comprimento_perfil.grid(row=4, column=1, padx=20, pady=20)
        
        
        self.bt_salvar_perfil = Button(self.cadastro_perfil, text="Salvar", command=self.event_bt_salvar)
        self.bt_salvar_perfil.grid(row=5, column=0, padx=20, pady=20, sticky=E)
        
        self.bt_cancelar_perfil = Button(self.cadastro_perfil, text="Cancelar", command=self.event_bt_cancelar)
        self.bt_cancelar_perfil.grid(row=5, column=1, padx=20, pady=20, sticky=E)   
        
        return self.cadastro_perfil.mainloop()
 
    
    def event_bt_cancelar(self):
        self.cadastro_perfil.destroy()
        
    
    def event_bt_salvar(self):
        codigo = self.entry_codigo_perfil.get()
        descricao = self.entry_descricao_perfil.get()
        kg_metro = self.entry_kg_metro_perfil.get()
        linha = self.combobox_linha_perfil.get()
        comprimento = self.entry_comprimento_perfil.get()
        
       
        """
        TODO CRIAR UMA FUNCAO QUE TROQUE A VIRGULA POR PONTO, PRINCIPALMENTE NO CAMPO KG_METRO
        """ 
        
        self.conexao.inserted_values = (codigo, descricao, kg_metro, linha, comprimento)
        
        self.conexao.insert_perfil()

#chama = Perfil().chama_tela_cadastro_perfil()
