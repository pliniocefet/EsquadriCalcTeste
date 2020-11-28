
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from ui_tela_cadastro_perfil import Ui_tela_cadastro_perfil

class TestePerfil(QtWidgets.QMainWindow, Ui_tela_cadastro_perfil):

    def __init__(self):
        super(TestePerfil, self).__init__()
        self.setupUi(self)
        self.app = None
        self.tela_cadastro_perfil = None

    
    def chama_tela_teste_perfil(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.tela_cadastro_perfil = TestePerfil()
        tela_cadastro_perfil.show()
        sys.exit(app.exec_())
    
chama = TestePerfil().chama_tela_teste_perfil()