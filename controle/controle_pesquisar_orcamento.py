from PyQt5.QtWidgets import QMainWindow
from view.tela_pesquisar_orcamento import Ui_tela_pesquisar_orcamento

#from model.model_cliente import *

class ControlePesquisarOrcamento(QMainWindow):

    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE PESQUISAR ORÇAMENTOS
        self.tela_pesquisar_orcamento = Ui_tela_pesquisar_orcamento()
        self.tela_pesquisar_orcamento.setupUi(self)
