import tkinter as tk
from tkinter import ttk


#def callbackFunc(event):
#    print(valor.get())

def botao():
    texto.set(valor.get()) # seta o valor do combobox na caixa de texto pressionando o botao


app = tk.Tk()
app.geometry('200x100')

labelTop = tk.Label(app, text="Choose your favourite month")
labelTop.grid(column=0, row=0)
valor = tk.StringVar()
comboExample = ttk.Combobox(app, textvariable=valor)
comboExample['values'] = ["January", "February", "March", "April"]
comboExample.grid(column=0, row=1)
comboExample.current(0)

texto = tk.StringVar()
et1 = tk.Entry(app, width=10, textvariable=texto)
et1.grid()

bt = tk.Button(app, text='ok', command=botao)
bt.grid()

#comboExample.bind("<<ComboboxSelected>>", callbackFunc)

app.mainloop()
