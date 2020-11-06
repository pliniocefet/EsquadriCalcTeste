from tkinter import *
from tkinter import messagebox
from conexao_perfil import ConexaoPerfil
from tkinter import ttk


class PesquisarPerfil:

	def __init__(self):

		self.conexao = ConexaoPerfil()
		self.lista_selecionados = []

	"""
	Metodo para centralizar a tela
	"""
	def centraliza_janela(self, instancia_tk):
	    largura_janela = instancia_tk.winfo_reqwidth()
	    altura_janela = instancia_tk.winfo_reqheight()
	    posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
	    posicao_y = int((instancia_tk.winfo_screenheight() / 3) - (altura_janela))

	    instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


	def chama_tela_pesquisar_perfil(self):

		self.pesquisar_perfil = Tk()
		self.centraliza_janela(self.pesquisar_perfil)
		self.pesquisar_perfil.geometry("510x200")
		self.pesquisar_perfil.title("Pesquisar perfil")
		
		# BOTÃO FILTRAR
		self.bt_filtrar = Button(self.pesquisar_perfil, text="Filtrar", command=self.event_bt_filtrar)
		self.bt_filtrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

		# ENTRY FILTRAR
		self.entry_filtrar = Entry(self.pesquisar_perfil, width=30)
		self.entry_filtrar.grid(row=0, column=1, pady=10, sticky=W)

		# TABELA DA PESQUISA
		self.tabela_resultado = ttk.Treeview(self.pesquisar_perfil, height=5, show="headings")
		self.tabela_resultado["columns"] = ("codigo", "descricao","kg/m", "linha")
		self.tabela_resultado.column("codigo", width=60)
		self.tabela_resultado.column("descricao", width=230)
		self.tabela_resultado.column("kg/m", width=50)
		self.tabela_resultado.column("linha", width=80)
		self.tabela_resultado.heading("codigo", text="Código", anchor="w")
		self.tabela_resultado.heading("descricao", text="Descrição", anchor="w")
		self.tabela_resultado.heading("kg/m", text="Kg/m", anchor="w")
		self.tabela_resultado.heading("linha", text="Linha", anchor="w")
		self.tabela_resultado.grid(row=1, column=0, columnspan=5, rowspan=3, padx=10, pady=10)

		# BOTÃO INSERIR
		self.bt_inserir = Button(self.pesquisar_perfil, text="Inserir", command=self.event_bt_inserir)
		self.bt_inserir.grid(row=1, column=5, pady=10, sticky=N)

		# BOTÃO CANCELAR
		self.bt_cancelar = Button(self.pesquisar_perfil, text="Cancelar", command=self.pesquisar_perfil.destroy)
		self.bt_cancelar.grid(row=2, column=5, sticky=N)

		self.pesquisar_perfil.mainloop()


	"""
	MOSTRA O RESULTADO DA PESQUISA PREENCHENDO A TABELA
	"""
	def event_bt_filtrar(self):

		# verifica se a tabela contém algum item pesquisado
		valor = self.tabela_resultado.get_children()

		# limpa a tabela quando fizer uma nova busca
		for item in valor:
			self.tabela_resultado.delete(item)

		if self.entry_filtrar.get() == "":
			messagebox.showinfo("Atenção!", "Faça uma busca para inserir um perfil")
	        
		else:

			pesquisa = "'%"+self.entry_filtrar.get()+"%'"

			self.conexao.valor_procurado = pesquisa
			resultado = self.conexao.pesquisar_perfil_produto()

			codigo = ""
			descricao = ""
			kgmetro = ""
			linha = ""
	        
			for valor in resultado:
				codigo = valor[0]
				descricao = valor[1]
				kgmetro = valor[2]
				linha = valor[3]
	        
				self.tabela_resultado.insert("","end", text="", values=(codigo, descricao, kgmetro, linha))

	def event_bt_inserir(self):

		self.selecionados = self.tabela_resultado.selection()

		for valor in self.selecionados:
			itens_selecionados = self.tabela_resultado.item(valor)["values"]
			self.lista_selecionados.append(itens_selecionados.copy())
		
		self.pesquisar_perfil.destroy()
		

 
#chama = PesquisarPerfil().chama_tela_pesquisar_perfil()