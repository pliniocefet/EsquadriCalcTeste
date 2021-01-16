from PyQt5.QtWidgets import QMainWindow, QApplication
from view.tela_principal import Ui_MainWindow_principal
from controle.controle_novo_orcamento import ControleNovoOrcamento
from controle.controle_cadastro_perfil import ControleCadastroPerfil


class ControlePrincipal(QMainWindow):
    """
        Classe que controla a tela principal do Software
        Aqui se manipula todas as telas que estão na view
        Executando metodos da camada Model se necessário
    """

    def __init__(self):
        super().__init__()
        self.tela_principal = Ui_MainWindow_principal()
        self.tela_principal.setupUi(self)

        # INSTACIA DO MENU NOVO ORÇAMENTO
        self.novo_orcamento = ControleNovoOrcamento()
        
        # INSTANCIA DO MENO CADASTRO PERFIL
        self.cadastro_perfil = ControleCadastroPerfil()

        #### AÇÕES ####
        # CHAMA O METODO PARA FECHAR O SISTEMA
        self.tela_principal.actionSair.triggered.connect(self.menu_sair)

        # CHAMA A TELA DE NOVO ORÇAMENTO
        self.tela_principal.actionNovo_Orcamento.triggered.connect(self.menu_novo_orcamento)

        # CHAMA A TELA DE CADASTRO DE PERFIL
        self.tela_principal.actionCadastro_de_Aluminios.triggered.connect(self.menu_cadastro_perfil)

    def menu_novo_orcamento(self):
        self.novo_orcamento.show()

    def menu_cadastro_perfil(self):
        self.cadastro_perfil.show()

    def menu_sair(self):
        self.close()

