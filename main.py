from PyQt5.QtWidgets import QApplication, QMainWindow

from telas_ui.tela_login import Ui_MainWindow
from model.model_login import ModelLogin
from tela_principal import TelaPrincipal
import sys


class Login(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.model_login = ModelLogin()
		self.tela_principal = TelaPrincipal()

		### AÇÃO DO BOTÃO LOGIN ###
		self.ui.pushButton_login.clicked.connect(self.verifica_usuario)

	
	def verifica_usuario(self):
		if self.model_login.event_bt_login(self.ui.lineEdit_user.text(), self.ui.lineEdit_password.text()):
			self.hide()
			self.tela_principal.chama_tela_principal()
			
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	login = Login()
	login.show()
	sys.exit(app.exec_())


