from tkinter import *
from tkinter import ttk
from conexao_produto import ConexaoProduto
from pesquisar_perfil import PesquisarPerfil


class Produto:

    def __init__(self):
        self.cadastro_produto = None
        self.pesquisar_perfil = PesquisarPerfil()


        self.bt_salvar_produto = None
        self.bt_cancelar_produto = None
        self.lb_codigo_produto = None
        self.lb_descricao_produto = None
        self.lb_linha_produto = None
        self.combobox_linha_produto = None
        self.tb_perfil_produto = None
        self.tb_acessorio_produto = None


        # Instancia para conexão com banco de dados
        self.conexao = ConexaoProduto()

    """
    Metodo para centralizar a tela
    """
    def centraliza_janela(self, instancia_tk):
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 3) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


    def inserir_produto(self):
        codigo = self.entry_codigo_produto.get()
        descricao = self.entry_descricao_produto.get()
        linha = self.combobox_linha_produto.get()

        self.conexao.inserted_values = (codigo, descricao, linha)
        self.conexao.insert_produto()


    def inserir_perfil(self):
        valor = self.pesquisar_perfil.event_bt_inserir()
        print(valor)



    def chama_tela_cadastro_produto(self):
        # Instancia de Tk()
        self.cadastro_produto = Tk()

        # Confgurações da tela
        self.cadastro_produto.title("Cadastro de Produtos")
        self.cadastro_produto.geometry("600x600")
        self.centraliza_janela(self.cadastro_produto)

        # LABEL CODIGO
        self.lb_codigo_produto = Label(self.cadastro_produto, text="Código do produto:")
        self.lb_codigo_produto.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # ENTRY CODIGO
        self.entry_codigo_produto = Entry(self.cadastro_produto)
        self.entry_codigo_produto.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # LABEL DESCRICAO
        self.lb_descricao_produto = Label(self.cadastro_produto, text="Descrição:")
        self.lb_descricao_produto.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # ENTRY DESCRICAO
        self.entry_descricao_produto = Entry(self.cadastro_produto, width=45)
        self.entry_descricao_produto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # LABEL LINHA
        self.lb_linha_produto = Label(self.cadastro_produto, text="Linha:")
        self.lb_linha_produto.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        # COMBOBOX LINHA
        self.combobox_linha_produto = ttk.Combobox(self.cadastro_produto, width=18)
        self.combobox_linha_produto["values"] = ("Linha Suprema", "Linha Gold", "Linha Convencional", "Linha 25", "Linha 30")
        self.combobox_linha_produto.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        # FRAME DA TABELA DE PERFIS
        self.frame_tabela_perfil = Frame(self.cadastro_produto)
        self.lb_perfil_produto = Label(self.frame_tabela_perfil, text="PERFIS UTILIZADOS NESTE PRODUTO")
        self.lb_perfil_produto.grid(row=0, column=0, pady=5, sticky=E+W)
        self.frame_tabela_perfil.configure(height=100, width=850, pady=10)
        self.tb_perfil_produto = ttk.Treeview(self.frame_tabela_perfil, height=5, show="headings")
        self.tb_perfil_produto["columns"] = ("codigo", "descricao","medida", "quantidade")
        self.tb_perfil_produto.column("codigo", width=50)
        self.tb_perfil_produto.column("descricao", width=250)
        self.tb_perfil_produto.column("medida", width=80)
        self.tb_perfil_produto.column("quantidade", width=50)
        self.tb_perfil_produto.heading("codigo", text="Código", anchor="w")
        self.tb_perfil_produto.heading("descricao", text="Descrição", anchor="w")
        self.tb_perfil_produto.heading("medida", text="Medida", anchor="w")
        self.tb_perfil_produto.heading("quantidade", text="Quant", anchor="w")
        
        self.tb_perfil_produto.grid(row=1, column=0, padx=17, rowspan=3)

        # BOTÃO BUSCAR PERFIL
        self.bt_buscar_perfil = Button(self.frame_tabela_perfil, text="Buscar Perfil")
        self.bt_buscar_perfil.configure(command=self.pesquisar_perfil.chama_tela_pesquisar_perfil)
        self.bt_buscar_perfil.grid(row=1, column=1, sticky=W)

        # BOTÃO EXCLUIR PERFIL
        self.bt_excluir_perfil = Button(self.frame_tabela_perfil, text="Excluir Perfil")
        self.bt_excluir_perfil.grid(row=2, column=1, sticky=W)

        # BOTÃO EDITAR PERFIL
        self.bt_editar_perfil = Button(self.frame_tabela_perfil, text="Editar Perfil ")
        self.bt_editar_perfil.grid(row=3, column=1, sticky=W)

        self.frame_tabela_perfil.grid(row=5, column=0, padx=5, pady=5, columnspan=3, sticky=E+W)

        # FRAME DA TABELA DE ACESSÓRIOS
        self.frame_tabela_acessorio = Frame(self.cadastro_produto)
        self.lb_acessorio_produto = Label(self.frame_tabela_acessorio, text="ACESSÓRIOS UTILIZADOS NESTE PRODUTO")
        self.lb_acessorio_produto.grid(row=0, column=0, pady=5, sticky=E+W)
        self.frame_tabela_acessorio.configure(height=100, width=850, pady=10)
        self.tb_acessorio_produto = ttk.Treeview(self.frame_tabela_acessorio, height=5, show="headings")
        self.tb_acessorio_produto["columns"] = ("codigo", "descricao", "quantidade")
        self.tb_acessorio_produto.column("codigo", width=50)
        self.tb_acessorio_produto.column("descricao", width=300)
        self.tb_acessorio_produto.column("quantidade", width=80)
        self.tb_acessorio_produto.heading("codigo", text="Código", anchor="w")
        self.tb_acessorio_produto.heading("descricao", text="Descrição", anchor="w")
        self.tb_acessorio_produto.heading("quantidade", text="Quant", anchor="w")
        self.tb_acessorio_produto.grid(row=1, column=0, padx=17, rowspan=3)

        # BOTÃO BUSCAR ACESSORIO
        self.bt_buscar_acessorio = Button(self.frame_tabela_acessorio, text="Buscar Acessório")
        self.bt_buscar_acessorio.grid(row=1, column=1)

        # BOTÃO EXCLUIR ACESSORIO
        self.bt_excluir_acessorio = Button(self.frame_tabela_acessorio, text="Excluir Acessório")
        self.bt_excluir_acessorio.grid(row=2, column=1)

        # BOTÃO EDITAR ACESSORIO
        self.bt_editar_acessorio = Button(self.frame_tabela_acessorio, text="Editar Acessório")
        self.bt_editar_acessorio.grid(row=3, column=1)

        
        self.frame_tabela_acessorio.grid(row=8, column=0, padx=5, pady=5, columnspan=3, sticky=E+W)


        # BOTOES
        self.bt_salvar_produto = Button(self.cadastro_produto, text="  Salvar  ", command=self.inserir_produto)
        self.bt_salvar_produto.grid(row=9, column=0, padx=5, pady=20, sticky=E)

        self.bt_cancelar_produto = Button(self.cadastro_produto, text="  Cancelar  ", command=self.cadastro_produto.destroy)
        self.bt_cancelar_produto.grid(row=9, column=1, pady=20, columnspan=2, sticky=W)
       

        return self.cadastro_produto.mainloop()


    
#chama = Produto().chama_tela_cadastro_produto()