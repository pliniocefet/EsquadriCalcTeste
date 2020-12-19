

class ModelLogin():
	"""
		Classe responsável por validar o usuario e informar ao controle
	"""

	def __init__(self):
		self.usuario = ''
		self.senha = ''

	def showMessage(self, message, frame_error, label_error):
		frame_error.show()
		label_error.setText(message)

	def check_login(self, campo_usuario, campo_senha, save_user):
		self.usuario = ''
		self.senha = ''

		if not campo_usuario:
			self.usuario = ' User Empty '
		else:
			self.usuario = ''

		if not campo_senha:
			self.senha = ' Password Empty '
		else:
			self.senha = ''

		if self.usuario + self.senha != '':
			text = self.usuario + self.senha
			self.showMessage(text)
		else:
			text = ' Login Ok '
			if save_user:
				text = text + ' | Save user: Ok '
			self.showMessage(text)
