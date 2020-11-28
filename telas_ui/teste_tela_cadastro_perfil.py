
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_tela_cadastro_perfil import Ui_tela_cadastro_perfil

class TestePerfil(QtWidgets.QMainWindow, Ui_tela_cadastro_perfil):

    def __init__(self):
        super(TestePerfil, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    tela_cadastro_perfil = TestePerfil()
    tela_cadastro_perfil.show()
    sys.exit(app.exec_())
