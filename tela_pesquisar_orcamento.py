from tkinter import *
from tkinter import ttk

class Pesquisar:
    """ DEFINE A TELA DE PESQUISA DE ORÇAMENTOS """

    # METODO CONSTRUTOR DA CLASSE
    def __init__(self):
        self.tela_pesquisar = Tk()

        # LABEL DO CODIGO DE CONTROLE
        lb_controle = Label(self.tela_pesquisar, text='Cod.')
        lb_controle.place(x=5, y=5)

        # ENTRADA DE DADOS DO CODIGO DE CONTROLE
        # implementar para aceitar somente numeros
        entry_codigo = Entry(self.tela_pesquisar, width=5)
        entry_codigo.focus_force()
        entry_codigo.place(x=5, y=30)

        # LABEL DO NOME DO CLIENTE
        # implementar para aceitar somente letras
        lb_nome = Label(self.tela_pesquisar, text='Nome do Cliente:')
        lb_nome.place(x=100, y=5)

        # ENTRADA DE DADOS DO NOME DO CLIENTE
        entry_nome = Entry(self.tela_pesquisar, width=30)
        entry_nome.place(x=100, y=30)

        # LABEL DA DATA
        lb_data = Label(self.tela_pesquisar, text='Data:')
        lb_data.place(x=350, y=5)

        # ENTRADA DE DADOS DA DATA
        entry_data = Entry(self.tela_pesquisar, width=11)
        entry_data.place(x=350, y=30)

        # TABELA DA PESQUISA
        self.tb_pesquisa = ttk.Treeview(self.tela_pesquisar, height=3, show='headings')

        # NOME DE REFERENCIA(APELIDO) DAS COLUNAS
        self.tb_pesquisa['columns'] = ('codigo', 'nome', 'data', 'revisao', 'situacao', 'observacoes')

        # TAMANHO DAS COLUNAS
        self.tb_pesquisa.column('codigo', width=50)
        self.tb_pesquisa.column('nome', width=220)
        self.tb_pesquisa.column('data', width=80)
        self.tb_pesquisa.column('revisao', width=50)
        self.tb_pesquisa.column('situacao', width=120)
        self.tb_pesquisa.column('observacoes', width=250)

        # TITULOS DAS COLUNAS
        self.tb_pesquisa.heading('codigo', text='Código', anchor='w')
        self.tb_pesquisa.heading('nome', text='Nome', anchor='w')
        self.tb_pesquisa.heading('data', text='Data', anchor='w')
        self.tb_pesquisa.heading('revisao', text='Revisao', anchor='w')
        self.tb_pesquisa.heading('situacao', text='Situação', anchor='w')
        self.tb_pesquisa.heading('observacoes', text='Observações', anchor='w')

        # ITENS DA LISTA
        # TODO implementar para os itens aparecerem apos a busca
        self.tb_item = self.tb_pesquisa.insert('', '0', value=('0000',
                                                     'Plínio de Macedo Corrêa',
                                                     '15/08/2018',
                                                     'Rev 01',
                                                     'Aprovado',
                                                     'Fabricar Contramarcos'))

        self.tb_pesquisa.place(x=5, y=60)

        # BOTÃO PESQUISAR
        bt_pesquisar = Button(self.tela_pesquisar, text='Pesquisar', width=15)
        bt_pesquisar.place(x=20, y=160)

        # BOTÃO VISUALIZAR
        bt_visualizar = Button(self.tela_pesquisar, text='Visualizar', width=15)
        bt_visualizar.place(x=170, y=160)

        # BOTÃO ABRIR
        bt_abrir = Button(self.tela_pesquisar, text='Abrir', width=15)
        bt_abrir.place(x=330, y=160)

        # BOTÃO LIMPAR
        bt_limpar = Button(self.tela_pesquisar, text='Limpar', width=15, command=self.limpar)
        bt_limpar.place(x=490, y=160)

        # BOTÃO EXCLUIR
        bt_excluir = Button(self.tela_pesquisar, text='Excluir', width=15)
        bt_excluir.place(x=650, y=160)

        self.tela_pesquisar.title('Pesquisar Orçamentos')
        self.tela_pesquisar.geometry('800x200+400+150')

        self.tela_pesquisar.mainloop()

    def limpar(self):
        self.tb_pesquisa.delete(self.tb_item)
