from tkinter import *
from tela_ajuda import Ajuda
from tela_novo_orcamento import Orcamento
from tela_pesquisar_orcamento import Pesquisar
from tela_config_vidro import ConfiguraVidro


class TelaPrincipal:

    # DEFINE O CONTAINER DE TKINTER
    janela_principal = Tk()

    # CRIA O MENU PRINCIPAL
    barra_de_menu = Menu(janela_principal)
    janela_principal.config(menu=barra_de_menu)

    # ITENS DO MENU - 1° NIVEL
    menu_orcamento = Menu(barra_de_menu, tearoff=False)
    menu_orcamento.add_cascade(label='Novo Orçamento...', command=Orcamento)
    menu_orcamento.add_cascade(label='Pesquisar Orçamento', command=Pesquisar)
    menu_orcamento.add_cascade(label='Sair', command=janela_principal.destroy)
    
    # MENU CONFIGURAÇÃO
    menu_configuracao = Menu(barra_de_menu, tearoff=False)
    menu_configuracao.add_cascade(label='Configurar Vidros', command=ConfiguraVidro)
    menu_configuracao.add_cascade(label='Configurar Alumínios')
    menu_configuracao.add_cascade(label='Cálculos e Folgas')
    menu_configuracao.add_cascade(label='Valores')

    # MENU RELATÓRIOS
    menu_relatorios = Menu(barra_de_menu, tearoff=False)
    menu_relatorios.add_cascade(label='Relatórios de Orçamentos')
    menu_relatorios.add_cascade(label='Relatório de Vidros')
    menu_relatorios.add_cascade(label='Relatório de Alumínios')
    menu_relatorios.add_cascade(label='Relatório de Tipologias')

    # MENU AJUDA
    menu_ajuda = Menu(barra_de_menu, tearoff=False)
    menu_ajuda.add_cascade(label='Sobre', command=Ajuda)

    # ADICIONA OS MENUS NA BARRA DE MENU
    barra_de_menu.add_cascade(label='Orçamentos', menu=menu_orcamento)
    barra_de_menu.add_cascade(label='Configurações', menu=menu_configuracao)
    barra_de_menu.add_cascade(label='Relatórios', menu=menu_relatorios)
    barra_de_menu.add_cascade(label='Ajuda', menu=menu_ajuda)

    # DEFINE O TITULO DA TELA
    janela_principal.title('EsquadriCalc - Cálculo de Esquadrias de Aluminio')

    # DEFINE A DIMENSÃO E POSIÇÃO DA TELA
    janela_principal.geometry('500x500+400+100')
    janela_principal.resizable(width=FALSE, height=FALSE)
    janela_principal.mainloop()
