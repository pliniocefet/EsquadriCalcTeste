from tkinter import *
from tkinter import ttk

def recupera():
    setText.set(cbText.get())

tela_config_vidro = Tk()
tela_config_vidro.geometry('550x500+300+100')
tela_config_vidro.title('Configurações dos Vidros')

    # LABEL DE OPÇÕES DE VIDROS
lb_opcoes = Label(tela_config_vidro, text='Tipo')
lb_opcoes.place(x=5, y=5)

    # COMBOBOX DE OPÇOES DE VIDROS
cbText = StringVar()
cb_tipo_vidro = ttk.Combobox(tela_config_vidro, textvariable=cbText)
cb_tipo_vidro['values'] = ['Temperado', 'Comum', 'Laminado']
cb_tipo_vidro['state'] = 'readonly'
cb_tipo_vidro.place(x=5, y=25)

    # LABEL DA COR DOS VIDROS
lb_cor_vidro = Label(tela_config_vidro, text='Cor do vidro:')
lb_cor_vidro.place(x=180, y=5)

    # COMBOBOX DE CORES DE VIDROS
cb_cor_vidro = ttk.Combobox(tela_config_vidro, width=10)
cb_cor_vidro['values'] = ('incolor', 'fume', 'verde')
cb_cor_vidro['state'] = 'readonly'
cb_cor_vidro.place(x=180, y=25)

    # LABEL DE ESPESSURA DO VIDRO
lb_espessura_vidro = Label(tela_config_vidro, text='Espessura:')
lb_espessura_vidro.place(x=300, y=5)

    # COMBOBOX DE ESPESSURAS DO VIDRO
cb_espessura_vidro = ttk.Combobox(tela_config_vidro, width=10)
cb_espessura_vidro['values'] = ('3mm', '4mm', '5mm', '6mm', '8mm', '10mm')
cb_espessura_vidro['state'] = 'readonly'
cb_espessura_vidro.place(x=300, y=25)

    # LABEL DE TRATAMENTO
lb_tratamento_vidro = Label(tela_config_vidro, text='Tratamento:')
lb_tratamento_vidro.place(x=420, y=5)

    # COMBOBOX DE TRATAMENTO DOS VIDROS
cb_tratamento_vidro = ttk.Combobox(tela_config_vidro, width=15)
cb_tratamento_vidro['values'] = ('Jateado', 'Serigrafado', 'Acidato')
cb_tratamento_vidro['state'] = 'readonly'
cb_tratamento_vidro.place(x=420, y=25)

    # BOTÃO EDITAR PROPRIEDADES DO VIDRO
    # implementar para o click habilitar os campos de edição
bt_editar_opcoes_vidro = Button(tela_config_vidro, text='Editar', width=10, command=recupera)
bt_editar_opcoes_vidro.place(x=20, y=65)

    # BOTÃO NOVO VIDRO
    # implementar para o click habilitar os campos em branco
bt_novo_vidro = Button(tela_config_vidro, text='Novo', width=10)
bt_novo_vidro.place(x=120, y=65)

    # BOTÃO EXCLUIR VIDRO
    # implementar para o click confirmar a exclusão do registro
bt_excluir_vidro = Button(tela_config_vidro, text='Excluir', width=10)
bt_excluir_vidro.place(x=220, y=65)

    # BOTÃO PESQUISAR VIDRO
bt_pesquisar_vidro = Button(tela_config_vidro, text='Pesquisar', width=10)
bt_pesquisar_vidro.place(x=440, y=65)

    # LABEL DO TIPO DE VIDRO
label_tipo_vidro = Label(tela_config_vidro, text='Tipo:')
label_tipo_vidro.place(x=10, y=110)

    # ENTRADA DE DADOS DO CAMPO TIPO DE VIDRO
setText = StringVar()
entry_tipo_vidro = Entry(tela_config_vidro, textvariable=setText, width=20)
entry_tipo_vidro.place(x=45, y=110)

    # LABEL DA COR DO VIDRO
label_cor_vidro = Label(tela_config_vidro, text='Cor:')
label_cor_vidro.place(x=180, y=110)

    # ENTRADA DE DADOS DA COR DO VIDRO
entry_cor_vidro = Entry(tela_config_vidro, width=10, state='disable')
entry_cor_vidro.place(x=210, y=110)

    # LABEL DA ESPESSURA DO VIDRO
label_espessura_vidro = Label(tela_config_vidro, text='Espessura:')
label_espessura_vidro.place(x=290, y=110)

    # ENTRADA DE DADOS DA ESPESSURA
entry_espesssura_vidro = Entry(tela_config_vidro, width=10, state='disable')
entry_espesssura_vidro.place(x=350, y=110)

    # LABEL DO TRATAMENTO
label_tratamento_vidro = Label(tela_config_vidro, text='Trat.')
label_tratamento_vidro.place(x=425, y=110)

    # ENTRADA DE DADOS DO TRATAMENTO
entry_tratamento_vidro = Entry(tela_config_vidro, width=12, state='disable')
entry_tratamento_vidro.place(x=455, y=110)

    # LABEL DO KG/M
label_peso_vidro = Label(tela_config_vidro, text='Kg/m2:')
label_peso_vidro.place(x=10, y=145)

    # ENTRADA DE DADOS DO PESO DO VIDRO
    # implementar metodo para calcular o peso do vidro de acordo com a espessura informada
entry_peso_vidro = Entry(tela_config_vidro, width=10, state='disable')
entry_peso_vidro.place(x=55, y=145)
tela_config_vidro.mainloop()
