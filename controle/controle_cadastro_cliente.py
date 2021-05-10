from PyQt5.QtWidgets import QMainWindow
from view.tela_cadastro_cliente import Ui_tela_cadastro_cliente

#from model.model_cliente import *

class ControleCadastroCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE CLIENTES
        self.tela_cadastro_cliente = Ui_tela_cadastro_cliente()
        self.tela_cadastro_cliente.setupUi(self)

