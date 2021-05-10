from PyQt5.QtWidgets import QApplication, QMainWindow
from view.tela_cadastro_perfil import Ui_tela_cadastro_perfil
from model.model_perfil import *

class ControleCadastroPerfil(QMainWindow):
	
	def __init__(self):
		super().__init__()
		# CHAMA A TELA DE CADASTRO DE PERFIS
		self.tela_cadastro_perfil = Ui_tela_cadastro_perfil()
		self.tela_cadastro_perfil.setupUi(self)

		### AÇÕES ###
		# QUANDO O BOTÃO CANCELAR FOR CLICADO
		self.tela_cadastro_perfil.pushButton_cancelar.clicked.connect(self.botao_cancelar)

		# QUANDO O BOTÃO NOVO FOR CLICADO
		self.tela_cadastro_perfil.pushButton_novo.clicked.connect(self.botao_novo)

		# QUANDO O BOTÃO SALVAR FOR CLICADO
		self.tela_cadastro_perfil.pushButton_salvar.clicked.connect(self.botao_salvar)

	
	def botao_cancelar(self):
		self.close()
	
	def botao_novo(self):
		self.tela_cadastro_perfil.lineEdit_codigo.setEnabled(True)
		self.tela_cadastro_perfil.lineEdit_descricao.setEnabled(True)
		self.tela_cadastro_perfil.lineEdit_peso.setEnabled(True)
		self.tela_cadastro_perfil.comboBox_linha.setEnabled(True)
		self.tela_cadastro_perfil.lineEdit_comprimento.setEnabled(True)
		self.tela_cadastro_perfil.pushButton_salvar.setEnabled(True)

	def botao_salvar(self):
		codigo = self.tela_cadastro_perfil.lineEdit_codigo.text()
		descricao = self.tela_cadastro_perfil.lineEdit_descricao.text()
		linha = self.tela_cadastro_perfil.comboBox_linha.currentText()
		peso = float(self.tela_cadastro_perfil.lineEdit_peso.text())
		comprimento = self.tela_cadastro_perfil.lineEdit_comprimento.text()

		lista_inserir = (codigo, descricao, peso, linha, comprimento)
		conexao = ModelPerfil()
		conexao.insert_perfil(lista_inserir)

		# LIMPAR CAMPOS
		self.tela_cadastro_perfil.lineEdit_codigo.setText("")
		self.tela_cadastro_perfil.lineEdit_codigo.setEnabled(False)
		self.tela_cadastro_perfil.lineEdit_descricao.setText("")
		self.tela_cadastro_perfil.lineEdit_descricao.setEnabled(False)
		self.tela_cadastro_perfil.lineEdit_peso.setText("")
		self.tela_cadastro_perfil.lineEdit_peso.setEnabled(False)
		self.tela_cadastro_perfil.comboBox_linha.setEnabled(False)
		self.tela_cadastro_perfil.lineEdit_comprimento.setText("")
		self.tela_cadastro_perfil.lineEdit_comprimento.setEnabled(False)
		self.tela_cadastro_perfil.pushButton_salvar.setEnabled(False)
		self.tela_cadastro_perfil.pushButton_novo.setEnabled(True)
