from tkinter import *
from tkinter import ttk


class ConfiguraVidro:

    def recupera(self):
        print(self.cbText.get())

    def __init__(self):
        self.tela_config_vidro = Tk()
        self.tela_config_vidro.geometry('550x500+300+100')
        self.tela_config_vidro.title('Configurações dos Vidros')

        # LABEL DE OPÇÕES DE VIDROS
        self.lb_opcoes = Label(self.tela_config_vidro, text='Tipo')
        self.lb_opcoes.place(x=5, y=5)

        # COMBOBOX DE OPÇOES DE VIDROS
        self.cbText = StringVar()
        self.cb_tipo_vidro = ttk.Combobox(self.tela_config_vidro, textvariable=self.cbText)
        self.cb_tipo_vidro['values'] = ['Temperado', 'Comum', 'Laminado']
        self.cb_tipo_vidro['state'] = 'readonly'
        self.cb_tipo_vidro.place(x=5, y=25)

        # LABEL DA COR DOS VIDROS
        self.lb_cor_vidro = Label(self.tela_config_vidro, text='Cor do vidro:')
        self.lb_cor_vidro.place(x=180, y=5)

        # COMBOBOX DE CORES DE VIDROS
        self.cb_cor_vidro = ttk.Combobox(self.tela_config_vidro, width=10)
        self.cb_cor_vidro['values'] = ('incolor', 'fume', 'verde')
        self.cb_cor_vidro['state'] = 'readonly'
        self.cb_cor_vidro.place(x=180, y=25)

        # LABEL DE ESPESSURA DO VIDRO
        self.lb_espessura_vidro = Label(self.tela_config_vidro, text='Espessura:')
        self.lb_espessura_vidro.place(x=300, y=5)

        # COMBOBOX DE ESPESSURAS DO VIDRO
        self.cb_espessura_vidro = ttk.Combobox(self.tela_config_vidro, width=10)
        self.cb_espessura_vidro['values'] = ('3mm', '4mm', '5mm', '6mm', '8mm', '10mm')
        self.cb_espessura_vidro['state'] = 'readonly'
        self.cb_espessura_vidro.place(x=300, y=25)

        # LABEL DE TRATAMENTO
        self.lb_tratamento_vidro = Label(self.tela_config_vidro, text='Tratamento:')
        self.lb_tratamento_vidro.place(x=420, y=5)

        # COMBOBOX DE TRATAMENTO DOS VIDROS
        self.cb_tratamento_vidro = ttk.Combobox(self.tela_config_vidro, width=15)
        self.cb_tratamento_vidro['values'] = ('Jateado', 'Serigrafado', 'Acidato')
        self.cb_tratamento_vidro['state'] = 'readonly'
        self.cb_tratamento_vidro.place(x=420, y=25)

        # BOTÃO EDITAR PROPRIEDADES DO VIDRO
        # implementar para o click habilitar os campos de edição
        self.bt_editar_opcoes_vidro = Button(self.tela_config_vidro, text='Editar', width=10, command=self.recupera)
        self.bt_editar_opcoes_vidro.place(x=20, y=65)

        # BOTÃO NOVO VIDRO
        # implementar para o click habilitar os campos em branco
        self.bt_novo_vidro = Button(self.tela_config_vidro, text='Novo', width=10)
        self.bt_novo_vidro.place(x=120, y=65)

        # BOTÃO EXCLUIR VIDRO
        # implementar para o click confirmar a exclusão do registro
        self.bt_excluir_vidro = Button(self.tela_config_vidro, text='Excluir', width=10)
        self.bt_excluir_vidro.place(x=220, y=65)

        # BOTÃO PESQUISAR VIDRO
        self.bt_pesquisar_vidro = Button(self.tela_config_vidro, text='Pesquisar', width=10)
        self.bt_pesquisar_vidro.place(x=440, y=65)

        # LABEL DO TIPO DE VIDRO
        self.label_tipo_vidro = Label(self.tela_config_vidro, text='Tipo:')
        self.label_tipo_vidro.place(x=10, y=110)

        # ENTRADA DE DADOS DO CAMPO TIPO DE VIDRO
        self.setText = StringVar()
        self.entry_tipo_vidro = Entry(self.tela_config_vidro, textvariable=self.setText, width=20)
        self.entry_tipo_vidro.place(x=45, y=110)

        # LABEL DA COR DO VIDRO
        self.label_cor_vidro = Label(self.tela_config_vidro, text='Cor:')
        self.label_cor_vidro.place(x=180, y=110)

        # ENTRADA DE DADOS DA COR DO VIDRO
        self.entry_cor_vidro = Entry(self.tela_config_vidro, width=10, state='disable')
        self.entry_cor_vidro.place(x=210, y=110)

        # LABEL DA ESPESSURA DO VIDRO
        self.label_espessura_vidro = Label(self.tela_config_vidro, text='Espessura:')
        self.label_espessura_vidro.place(x=290, y=110)

        # ENTRADA DE DADOS DA ESPESSURA
        self.entry_espesssura_vidro = Entry(self.tela_config_vidro, width=10, state='disable')
        self.entry_espesssura_vidro.place(x=350, y=110)

        # LABEL DO TRATAMENTO
        self.label_tratamento_vidro = Label(self.tela_config_vidro, text='Trat.')
        self.label_tratamento_vidro.place(x=425, y=110)

        # ENTRADA DE DADOS DO TRATAMENTO
        self.entry_tratamento_vidro = Entry(self.tela_config_vidro, width=12, state='disable')
        self.entry_tratamento_vidro.place(x=455, y=110)

        # LABEL DO KG/M
        self.label_peso_vidro = Label(self.tela_config_vidro, text='Kg/m2:')
        self.label_peso_vidro.place(x=10, y=145)

        # ENTRADA DE DADOS DO PESO DO VIDRO
        # implementar metodo para calcular o peso do vidro de acordo com a espessura informada
        self.entry_peso_vidro = Entry(self.tela_config_vidro, width=10, state='disable')
        self.entry_peso_vidro.place(x=55, y=145)

        self.tela_config_vidro.mainloop()
