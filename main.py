from PyQt5.QtWidgets import QApplication, QMainWindow

from controle.controle_principal import ControlePrincipal
from view.tela_login import Ui_MainWindow
import sys


class Main(QMainWindow):
	"""
		Classe que controla o Login do Software
		Classe com o main - primeiro a ser executado
	"""
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# CONFIGURAÇÕES INICIAIS
		self.ui.pushButton_error.setText('')

		# TELA PRINCIPAL
		self.tela_principal = ControlePrincipal()

		# AÇÃO DO BOTÃO lOGIN
		# Chama o metodo que exibe a tela principal
		self.ui.pushButton_login.clicked.connect(self.chama_tela_principal)

	def validar_usuario(self):
		pass

	def chama_tela_principal(self):
		self.hide()
		self.tela_principal.show()

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())
