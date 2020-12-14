

class ModelLogin():

	def showMessage(message):
			self.frame_error.show()
			self.label_error.setText(message)


	def check_login(self):
		usuario = ''
		senha = ''

		if not self.lineEdit_user.text():
			usuario = ' User Empty '
		else:
			usuario = ''

		if not self.lineEdit_password.text():
			senha = ' Password Empty '
		else:
			senha = ''

		if usuario + senha != '':
			text = usuario + senha
			showMessage(text)
		else:
			text = ' Login Ok '
			if self.checkBox_save_user.isChecked():
				text = text + ' | Save user: Ok '
			showMessage(text)