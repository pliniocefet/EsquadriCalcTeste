from PyQt5.QtWidgets import QMainWindow, QApplication
from view.tela_principal import Ui_MainWindow_principal
from controle.controle_novo_orcamento import ControleNovoOrcamento


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

        self.tela_principal.actionNovo_Orcamento.triggered.connect(self.menu_novo_orcamento)

    def menu_novo_orcamento(self):
        self.novo_orcamento.show()

