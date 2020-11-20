from tkinter import *
import webbrowser

class Ajuda:
    """ DEFINE A TELA DE AJUDA """
    # METODO CONSTRUTOR
    def __init__(self):
        self.tela_ajuda = None
        self.lb_descritivo = None
        self.lb_email = None


    def abrir_email(self, event):
        webbrowser.open_new_tab("http://www.gmail.com")


    def centraliza_janela(self, instancia_tk):
        """
        Metodo para centralizar a janela na tela
        """
        largura_janela = instancia_tk.winfo_reqwidth()
        altura_janela = instancia_tk.winfo_reqheight()
        # print("largura da tela: ", largura_janela, "altura da tela: ", altura_janela)

        posicao_x = int((instancia_tk.winfo_screenwidth() / 2.5) - (largura_janela))
        posicao_y = int((instancia_tk.winfo_screenheight() / 2) - (altura_janela))

        instancia_tk.geometry("+{}+{}".format(posicao_x, posicao_y))


    def chama_tela_ajuda(self):
        self.tela_ajuda = Tk()
        self.tela_ajuda.title('Sobre o EsquadriCalc')
        self.centraliza_janela(self.tela_ajuda)
        self.tela_ajuda.geometry('300x120')

        self.lb_descritivo = Label(self.tela_ajuda)
        descritivo = 'EsquadriCalc\nSistema para Calculo de Esquadrias de Aluminio\n'
        versao = 'V 1.0\n\n'
        desenvolvedor = 'Desenvolvedor:\nPlínio de Macedo Corrêa'
        email = 'plinio.cefet@gmail.com'
     
        self.lb_descritivo['text'] = descritivo + versao + desenvolvedor
        self.lb_descritivo.pack()
        self.lb_email = Label(self.tela_ajuda, text=email, fg='blue', cursor='hand2')
        self.lb_email.pack()
        self.lb_email.bind("<Button-1>", self.abrir_email)

        self.tela_ajuda.resizable(width=FALSE, height=FALSE)
        self.tela_ajuda.mainloop()