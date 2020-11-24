from tkinter import *
from tela_ajuda import Ajuda
from tela_novo_orcamento import Orcamento
from tela_pesquisar_orcamento import Pesquisar
from tela_config_vidro import ConfiguraVidro
from perfil import Perfil
from acessorio import Acessorio
from vidro import Vidro
from produto import Produto


class TelaPrincipal:

    def __init__(self):
        # Instancia de Tk
        self.tela_principal = None
        self.menu_principal = None
        self.submenu_orcamento = None
        self.submenu_cadastro = None
        self.perfil = Perfil()
        self.acessorio = Acessorio()
        self.vidro = Vidro()
        self.produto = Produto()
        self.orcamento = Orcamento()
        self.configurar_vidro = ConfiguraVidro()
        self.tela_ajuda = Ajuda()

        self.usuario_logado = None

    
    def centraliza_janela(self, instancia_tk):
        """
        Metodo para centralizar a janela na tela
        """
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)

        posicao_x = int((instancia_tk.winfo_screenwidth() / 2.5) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 2) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))

    
    def chama_tela_principal(self):
        """
        Chama a tela principal do programa
        """
        self.tela_principal = Tk()

        # Configuraçõe da tela
        self.tela_principal.title(f"Cálculo de Esquadrias de Alumínio *** Usuario Logado: {self.usuario_logado} ***")
        self.centraliza_janela(self.tela_principal)
        self.tela_principal.geometry("600x400")

        # Cria o menu superior principal
        self.menu_principal = Menu(self.tela_principal)

        # Cria submenus em Orçamentos
        self.submenu_orcamento = Menu(self.menu_principal, tearoff=0)
        self.submenu_orcamento.add_command(label="Novo Orçamento", command=self.orcamento.chama_tela_novo_orcamento)
        self.submenu_orcamento.add_command(label="Buscar Orçamento")
        self.submenu_orcamento.add_command(label="Sair", command=sys.exit)

        """
            TODO Vincular a tela de busca de orçamento com a tela principal. Ao clicar no menu chamar a tela de busca
        """
        
        # Cria submenus em Cadastro
        self.submenu_cadastro = Menu(self.menu_principal, tearoff=0)
        self.submenu_cadastro.add_command(label="Cadastrar perfil", command=self.perfil.chama_tela_cadastro_perfil)
        self.submenu_cadastro.add_command(label="Cadastrar acessorio", command=self.acessorio.chama_tela_cadastro_acessorio)
        self.submenu_cadastro.add_command(label="Cadastrar vidro", command=self.vidro.chama_tela_cadastro_vidro)
        self.submenu_cadastro.add_command(label="Cadastrar Produto", command=self.produto.chama_tela_cadastro_produto)

        # Cria submenus em Configurações
        self.submenu_configuracoes = Menu(self.menu_principal, tearoff=0)
        self.submenu_configuracoes.add_command(label='Configurar Vidro', command=self.configurar_vidro.chama_tela_config_vidro)
        self.submenu_configuracoes.add_command(label='Configurar Alumínio')
        self.submenu_configuracoes.add_command(label='Configurar Acessorio')
        self.submenu_configuracoes.add_command(label='Configurar Produto')
        
        """
            TODO Alterar a classe de configuração do vidro para o mesmo padrão das outras
            criar o metodo chama tela e chamar no commando do menu
        """

         # Cria submenus em Relatórios
        self.submenu_relatorios = Menu(self.menu_principal, tearoff=0)
        self.submenu_relatorios.add_command(label='Relatorio de Vidros')
        self.submenu_relatorios.add_command(label='Relatório de Perfis')
        self.submenu_relatorios.add_command(label='Relatório de Acessorios')
        self.submenu_relatorios.add_command(label='Relatório de Produtos')

         # Cria submenus em Ajuda
        self.submenu_ajuda = Menu(self.menu_principal, tearoff=0)
        self.submenu_ajuda.add_command(label='Sobre...', command=self.tela_ajuda.chama_tela_ajuda)

        # Adiciona os itens de menu ao menu principal
        self.menu_principal.add_cascade(label="Orçamento", menu=self.submenu_orcamento)
        self.menu_principal.add_cascade(label="Cadastro", menu=self.submenu_cadastro)
        self.menu_principal.add_cascade(label='Configurações', menu=self.submenu_configuracoes)
        self.menu_principal.add_cascade(label='Relatórios', menu=self.submenu_relatorios)
        self.menu_principal.add_cascade(label='Ajuda', menu=self.submenu_ajuda)

        self.tela_principal.config(menu=self.menu_principal)


        return self.tela_principal.mainloop()
    
#chama = TelaPrincipal().chama_tela_principal()