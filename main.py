from PyQt5.QtWidgets import QApplication, QMainWindow

from telas_ui.tela_login import Ui_MainWindow
import sys


class Login(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	login = Login()
	login.show()
	sys.exit(app.exec_())


