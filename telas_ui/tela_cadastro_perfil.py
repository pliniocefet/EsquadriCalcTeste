
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Perfil(QtWidgets.QMainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.form = uic.loadUi('telas_ui\\tela_cadastro_perfil.ui')


    def chama_tela_cadastro_perfil(self):
        self.form.show()

        def botao_salvar():
            self.form.lineEdit_descricao.setText('Preenche')

        def botao_limpar():
        	self.form.lineEdit_descricao.setText('')
	    	
        
        self.form.pushButton_salvar.clicked.connect(botao_salvar)
        self.form.pushButton_editar.clicked.connect(botao_limpar)
        self.app.exec_()



#chama = Perfil().chama_tela_cadastro_perfil()

