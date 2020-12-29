from model.conexao_usuario import ConexaoUsuario

class ModelLogin():
	"""
		Classe responsável por validar o usuario e informar ao controle
	"""

	def event_bt_login(self,login,senha):
		"""
			METODO QUE VERIFICA NO BANCO DE DADOS O NOME DO USUARIO E A SENHA
			BOTÃO LOGIN
		"""
		# Conexão com banco de dados
		self.conexao = ConexaoUsuario()

		usuario = self.conexao.buscar_user(login)
		user = None
		password = None

		if usuario != []:
			user = usuario[0][0]
			password = usuario[0][1]
		else:
			print("Atenção!", "Usuario ou senha invalida!! ")

		if user == login:
			if password == senha:
				print("Bem vindo", "Seja Bem vindo " + usuario[0][0].title())
				return True

			else:
				print("Atenção!", "Senha inválida! ")
				return False
		else:
			print("Atenção!", "Usuario não cadastrado!! ")
			return False