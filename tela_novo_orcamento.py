from tkinter import *
from tkinter import messagebox
import sys


class Orcamento:
    """ DEFINE A TELA DE NOVO ORÇAMENTO """

    def __init__(self):
        """
        Metodo construtor da classe Orçamento
        """
        self.tela_novo_orcamento = None
        self.lb_controle_orcamento = None
        self.lb_codigo = None
        self.lb_data = None
        self.lb_recupera_data = None
        self.lb_nome_cliente = None
        self.entry_nome = None
        self.lb_telefone = None
        self.entry_telefone = None
        self.lb_endereco = None
        self.entry_endereco = None
        self.lb_email = None
        self.entry_email = None
        self.lb_numero = None
        self.entry_numero = None
        self.lb_vendedor = None
        self.entry_vendedor = None
        self.lb_bairro = None
        self.entry_bairro = None
        self.lb_cidade = None
        self.entry_cidade = None
        self.bt_cancelar = None
        self.bt_salvar_orcamento = None

        # LABEL DA LINHA DE PRODUTOS
        #lb_linha_produtos = Label(self.tela_novo_orcamento, text='Linha de Produtos:')
        #lb_linha_produtos.place(x=100, y=295)

        # COMBOBOX LINHA DE PRODUTOS
        # implementar para ser opção obrigatoria
        #cb_linha_produtos = ttk.Combobox(self.tela_novo_orcamento, width=15)
        #cb_linha_produtos['values'] = ('Linha Suprema', 'Linha Gold',
        #                              'Linha 25', 'Linha 30')
        #cb_linha_produtos.place(x=100, y=320)

        # LABEL COR DO ALUMINIO
        #lb_cor_aluminio = Label(self.tela_novo_orcamento, text='Cor do Aluminio:')
        #lb_cor_aluminio.place(x=250, y=295)

        # COMBOBOX COR DO ALUMINIO
        # implementar para ser opção obrigatória
        #cb_cor_aluminio = ttk.Combobox(self.tela_novo_orcamento, width=22)
        #cb_cor_aluminio['values'] = ('Pintado Branco 9010', 'Pintado Preto', 'Anodizado Preto',
        #                             'Anodizado Bronze 1002', 'Anodizado Fosco')
        #cb_cor_aluminio.place(x=250, y=320)
        

           
    def centraliza_janela(self, instancia_tk):
        """
        Metodo para centralizar a tela
        """
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)

        posicao_x = int((instancia_tk.winfo_screenwidth() / 2) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 3) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


    def chama_tela_novo_orcamento(self):
        # Instancia de Tk()
        self.tela_novo_orcamento = Tk()

        # Configurações da tela de novo orçamento
        self.tela_novo_orcamento.title('Novo Orçamento')
        self.tela_novo_orcamento.geometry('510x430+400+150')
        self.centraliza_janela(self.tela_novo_orcamento)
        self.tela_novo_orcamento.resizable(width=FALSE, height=FALSE)

        # LABEL DE CONTROLE DE ORÇAMENTOS
        self.lb_controle_orcamento = Label(self.tela_novo_orcamento, text='Cód Controle:')
        self.lb_controle_orcamento.place(x=5, y=5)

        # LABEL DO NUMERO DE CONTROLE
        """ TODO
            implementar para o codigo ser sequencial
        """
        self.lb_codigo = Label(self.tela_novo_orcamento, text='0000')
        self.lb_codigo.place(x=85, y=5)

        # LABEL DA DATA
        self.lb_data = Label(self.tela_novo_orcamento, text='Data:')
        self.lb_data.place(x=320, y=5)

        # LABEL DO DIA
        self.lb_recupera_data = Label(self.tela_novo_orcamento, text='00/00/0000')
        self.lb_recupera_data.place(x=350, y=5)

        # LABEL DO NOME DO CLIENTE
        self.lb_nome_cliente = Label(self.tela_novo_orcamento, text='Nome do Cliente:')
        self.lb_nome_cliente.place(x=5, y=30)

        # COMPONENTE DE ENTRADA DE DADOS PARA O NOME
        """ TODO
            implementar para somente letras
            implementar para ser campo obrigatorio
        """
        self.entry_nome = Entry(self.tela_novo_orcamento, width=40)
        # Ao chamar a tela de novo orçamento o cursor ja fica em Nome do Cliente
        self.entry_nome.focus_force()
        self.entry_nome.place(x=5, y=55)

        # LABEL DO TELEFONE DO CLIENTE
        """ TODO
            implementar mascara de telefone
            implementar para ser campo obrigatorio
        """
        self.lb_telefone = Label(self.tela_novo_orcamento, text='Telefone de Contato:')
        self.lb_telefone.place(x=320, y=30)

        # ENTRADA DE DADOS PARA O TELEFONE
        """ TODO
            implementar para somente numeros
        """
        self.entry_telefone = Entry(self.tela_novo_orcamento, width=13)
        self.entry_telefone.place(x=320, y=55)

        # LABEL DO ENDEREÇO
        self.lb_endereco = Label(self.tela_novo_orcamento, text='Endereço:')
        self.lb_endereco.place(x=5, y=80)

        # ENTRADA DE DADOS PARA O ENDEREÇO
        self.entry_endereco = Entry(self.tela_novo_orcamento, width=40)
        self.entry_endereco.place(x=5, y=105)

        # LABEL DO EMAIL
        self.lb_email = Label(self.tela_novo_orcamento, text='Email:')
        self.lb_email.place(x=320, y=80)

        # ENTRADA DE DADOS PARA O EMAIL
        self.entry_email = Entry(self.tela_novo_orcamento, width=25)
        self.entry_email.place(x=320, y=105)

        # LABEL DO NUMERO
        self.lb_numero = Label(self.tela_novo_orcamento, text='Numero:')
        self.lb_numero.place(x=5, y=130)

        # ENTRADA DE DADOS PARA O NUMERO
        self.entry_numero = Entry(self.tela_novo_orcamento, width=5)
        self.entry_numero.place(x=5, y=155)

        # LABEL DO VENDEDOR
        self.lb_vendedor = Label(self.tela_novo_orcamento, text='Vendedor:')
        self.lb_vendedor.place(x=320, y=130)

        # ENTRADA DE DADOS PARA O VENDEDOR
        self.entry_vendedor = Entry(self.tela_novo_orcamento, width=20)
        self.entry_vendedor.place(x=320, y=155)

        # LABEL DO BAIRRO
        self.lb_bairro = Label(self.tela_novo_orcamento, text='Bairro:')
        self.lb_bairro.place(x=5, y=180)

        # ENTRADA DE DADOS PARA O BAIRRO
        self.entry_bairro = Entry(self.tela_novo_orcamento, width=30)
        self.entry_bairro.place(x=5, y=205)

        # LABEL DA CIDADE
        self.lb_cidade = Label(self.tela_novo_orcamento, text='Cidade:')
        self.lb_cidade.place(x=5, y=230)

        # ENTRADA DE DADOS CIDADE
        self.entry_cidade = Entry(self.tela_novo_orcamento, width=30)
        self.entry_cidade.place(x=5, y=255)

        # BOTÃO SALVAR
        """ TODO
            implementar - quando clicar em salvar fechar a tela de novo orçamento e abrir a tela de opçoes de tipologia
        """
        self.bt_salvar_orcamento = Button(self.tela_novo_orcamento, text='Salvar', width=15, command=self.event_bt_salvar_orcamento)
        self.bt_salvar_orcamento.place(x=120, y=380)

        # BOTÃO CANCELAR
        self.bt_cancelar = Button(self.tela_novo_orcamento, text='Cancelar', width=15, command=self.event_bt_cancelar)
        self.bt_cancelar.place(x=280, y=380)

        return self.tela_novo_orcamento.mainloop()


    def event_bt_cancelar(self):
        self.tela_novo_orcamento.destroy()



    def event_bt_salvar_orcamento(self):
        messagebox.showinfo("salvou","salvou")


chama = Orcamento().chama_tela_novo_orcamento()


"""
    TODO
    FALTA AINDA IMPLEMENTAR ALGUNS ITENS
    COMO MASCARAS PARA CADASTRO E O BOTÃO SALVAR
"""