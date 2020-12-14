from model.conexao_usuario import ConexaoUsuario

class ModelLogin():

	def __init__(self):
		self.usuario = None
		self.senha = None

		self.conexao = ConexaoUsuario()


	def event_bt_login(self, usuario_logado, senha_logado):

		self.usuario = self.conexao.buscar_user(usuario_logado)
		user = None
		senha = None

		# Se a lista de usuarios for diferente de vazia preenche os campos user e senha com os dados
		if self.usuario != []:
			user = self.usuario[0][0]
			senha = self.usuario[0][1]
		else:
			print("Usuario ou senha invalida!! ")

		if user == usuario_logado:
			if senha == senha_logado:
				print("Bem vindo", "Seja Bem vindo " + self.usuario[0][0].title())
				return True
			else:
				print("Atenção!", "Senha inválida! ")
		else:
			print("Atenção!", "Usuario não cadastrado!! ")
