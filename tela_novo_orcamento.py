from tkinter import *
from tkinter import messagebox


class Orcamento:
    """ DEFINE A TELA DE NOVO ORÇAMENTO """

    # METODO CONSTRUTOR DA CLASSE ORCAMENTO
    def __init__(self):
        self.tela_novo_orcamento = Tk()
        self.tela_novo_orcamento.title('Novo Orçamento')

        # LABEL DE CONTROLE DE ORÇAMENTOS
        lb_controle = Label(self.tela_novo_orcamento, text='Cód Controle:')
        lb_controle.place(x=5, y=5)

        # LABEL DO NUMERO DE CONTROLE
        # implementar para o codigo ser sequencial
        lb_codigo = Label(self.tela_novo_orcamento, text='0000')
        lb_codigo.place(x=85, y=5)

        # LABEL DA DATA
        lb_data = Label(self.tela_novo_orcamento, text='Data:')
        lb_data.place(x=320, y=5)

        # LABEL DO DIA
        lb_recupera_data = Label(self.tela_novo_orcamento, text='00/00/0000')
        lb_recupera_data.place(x=350, y=5)

        # LABEL DO NOME DO CLIENTE
        lb_nome_cliente = Label(self.tela_novo_orcamento, text='Nome do Cliente:')
        lb_nome_cliente.place(x=5, y=30)

        # COMPONENTE DE ENTRADA DE DADOS PARA O NOME
        # implementar para somente letras
        # implementar para ser campo obrigatorio
        entry_nome = Entry(self.tela_novo_orcamento, width=40)

        # Ao chamar a tela de novo orçamento o cursor ja fica em Nome do Cliente
        entry_nome.focus_force()
        entry_nome.place(x=5, y=55)

        # LABEL DO TELEFONE DO CLIENTE
        # implementar mascara de telefone
        # implementar para ser campo obrigatorio
        lb_telefone = Label(self.tela_novo_orcamento, text='Telefone de Contato:')
        lb_telefone.place(x=320, y=30)

        # ENTRADA DE DADOS PARA O TELEFONE
        # implementar para somente numeros
        entry_telefone = Entry(self.tela_novo_orcamento, width=13)
        entry_telefone.place(x=320, y=55)

        # LABEL DO ENDEREÇO
        lb_endereco = Label(self.tela_novo_orcamento, text='Endereço:')
        lb_endereco.place(x=5, y=80)

        # ENTRADA DE DADOS PARA O ENDEREÇO
        entry_endereco = Entry(self.tela_novo_orcamento, width=40)
        entry_endereco.place(x=5, y=105)

        # LABEL DO EMAIL
        lb_email = Label(self.tela_novo_orcamento, text='Email:')
        lb_email.place(x=320, y=80)

        # ENTRADA DE DADOS PARA O EMAIL
        entry_email = Entry(self.tela_novo_orcamento, width=25)
        entry_email.place(x=320, y=105)

        # LABEL DO NUMERO
        lb_numero = Label(self.tela_novo_orcamento, text='Numero:')
        lb_numero.place(x=5, y=130)

        # ENTRADA DE DADOS PARA O NUMERO
        entry_numero = Entry(self.tela_novo_orcamento, width=5)
        entry_numero.place(x=5, y=155)

        # LABEL DO VENDEDOR
        lb_vendedor = Label(self.tela_novo_orcamento, text='Vendedor:')
        lb_vendedor.place(x=320, y=130)

        # ENTRADA DE DADOS PARA O VENDEDOR
        entry_vendedor = Entry(self.tela_novo_orcamento, width=20)
        entry_vendedor.place(x=320, y=155)

        # LABEL DO BAIRRO
        lb_bairro = Label(self.tela_novo_orcamento, text='Bairro:')
        lb_bairro.place(x=5, y=180)

        # ENTRADA DE DADOS PARA O BAIRRO
        entry_bairro = Entry(self.tela_novo_orcamento, width=30)
        entry_bairro.place(x=5, y=205)

        # LABEL DA CIDADE
        lb_cidade = Label(self.tela_novo_orcamento, text='Cidade:')
        lb_cidade.place(x=5, y=230)

        # ENTRADA DE DADOS CIDADE
        entry_cidade = Entry(self.tela_novo_orcamento, width=30)
        entry_cidade.place(x=5, y=255)

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

        # BOTÃO SALVAR
        # implementar - quando clicar em salvar fechar a tela de novo orçamento
        # e abrir a tela de opçoes de tipologia
        bt_salvar = Button(self.tela_novo_orcamento, text='Salvar', width=15, command=self.bt_salvar_orcamento)
        bt_salvar.place(x=120, y=380)

        # BOTÃO CANCELAR
        # Ao clicar em cancelar fechar a tela de novo orçamento
        bt_cancelar = Button(self.tela_novo_orcamento, text='Cancelar', width=15,
                             command=self.tela_novo_orcamento.destroy)
        bt_cancelar.place(x=280, y=380)

        self.tela_novo_orcamento.geometry('510x430+400+150')
        self.tela_novo_orcamento.resizable(width=FALSE, height=FALSE)
        self.tela_novo_orcamento.mainloop()

    def bt_salvar_orcamento(self):
        messagebox.showinfo("salvou","salvou")



"""
    FALTA AINDA IMPLEMENTAR ALGUNS ITENS
    COMO MASCARAS PARA CADASTRO E O BOTÃO SALVAR
"""