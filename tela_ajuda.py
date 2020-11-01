from tkinter import *
import webbrowser

class Ajuda:
    """ DEFINE A TELA DE AJUDA """
    # METODO CONSTRUTOR
    def __init__(self):
        self.tela_ajuda = Tk()
        self.tela_ajuda.title('Sobre o EsquadriCalc')
        self.tela_ajuda.geometry('300x120+500+200')

        lb1 = Label(self.tela_ajuda)
        descritivo = 'EsquadriCalc\nSistema para Calculo de Esquadrias de Aluminio\n'
        versao = 'V 1.0\n\n'
        desenvolvedor = 'Desenvolvedor:\nPlínio de Macedo Corrêa'
        email = 'plinio.cefet@gmail.com'
        lb1['text'] = descritivo + versao + desenvolvedor
        lb1.pack()
        lb2 = Label(self.tela_ajuda, text=email, fg='blue', cursor='hand2')
        lb2.pack()
        lb2.bind("<Button-1>", abrir_email)

        self.tela_ajuda.resizable(width=FALSE, height=FALSE)
        self.tela_ajuda.mainloop()

def abrir_email(event):
    webbrowser.open_new_tab("http://www.gmail.com")
