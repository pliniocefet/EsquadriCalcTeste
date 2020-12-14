from telas_ui.tela_login import Ui_MainWindow
from model.model_login import ModelLogin
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class ControleLogin(QMainWindow):
	def __init__(self):
		super().__init__()
		self.tela_login = Ui_MainWindow()
		self.tela_login.setupUi(self)

		self.model_login = ModelLogin()
	



