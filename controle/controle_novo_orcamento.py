from PyQt5.QtWidgets import QMainWindow, QApplication
from view.tela_novo_orcamento import Ui_tela_novo_orcamento


class ControleNovoOrcamento(QMainWindow):

    def __init__(self):
        super().__init__()
        self.novo_orcamento = Ui_tela_novo_orcamento()
        self.novo_orcamento.setupUi(self)
