import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from telas_ui.tela_principal import Ui_MainWindow_principal


class TelaPrincipal(QMainWindow):
	def __init__(self):
		super().__init__()
		self.tela_principal = Ui_MainWindow_principal()
		self.tela_principal.setupUi(self)

		### AÇÃO DO MENU -> ORÇAMENTO -> SAIR ###
		# Fecha o sistema
		self.tela_principal.actionSair.triggered.connect(self.sair)

	"""
		TODO
		INCLUIR AQUI TODOS OS METODOS DE MANIPULAÇÃO DA CLASSE MODEL PARA A CLASSE VIEW 
		E VICE E VERSA
 	"""
	@QtCore.pyqtSlot() # PESQUISAR MAIS SOBRE ESTE DECORATOR (não sei bem ao certo para que serve)
	def sair(self):
		"""
			Metodo para fechar o sistema
		"""
		sys.exit()

		