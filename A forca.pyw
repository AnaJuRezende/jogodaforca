from tkinter import *
import random

sorteia = random.choice

x = open('Nomes.txt', 'r', encoding='utf-8')
lista = x.readlines()
x.close()

palavra = sorteia(lista).split('\n')[0].upper()
lista_letras = []
lista_traco = []
lista_erro = []
digito = []

for i in range(len(palavra)):
    lista_letras.append(palavra[i])
    lista_traco.append('__ ')

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title('Jogo da Forca')

        self.canvas = Canvas(root, width=200, height=400)
        self.canvas.pack(side=LEFT)

        self.frame = Frame(root)
        self.frame.pack(side=LEFT, padx=20)

        self.lista_letras = []
        self.lista_traco = []
        self.lista_erro = []
        self.digito = []

        with open('Nomes.txt', 'r', encoding='utf-8') as x:
            self.lista = x.readlines()

        self.palavra = random.choice(self.lista).strip().upper()

        for letra in self.palavra:
            self.lista_letras.append(letra)
            self.lista_traco.append('__ ')

        self.msg = Label(self.frame, text=self.lista_traco, font=('Arial', 18), fg='blue')
        self.msg.pack()

        self.caixa = StringVar()
        self.nom = Entry(self.frame, textvariable=self.caixa, font=('Arial', 14))
        self.nom.focus_force()
        self.nom.pack()
        self.nom.bind('<Return>', self.forca)

        self.msg2 = Label(self.frame, text='Letras Erradas: ', font=('Arial', 14), fg='red')
        self.msg2.pack()
        self.msg3 = Label(self.frame, text='', font=('Arial', 16))
        self.msg3.pack()

    def forca(self, event):
        letra = self.caixa.get().upper()[0]

        if letra in self.digito:
            self.caixa.set('')
            return

        if letra in self.lista_letras:
            self.digito.append(letra)
            for t in range(len(self.lista_letras)):
                if letra == self.lista_letras[t]:
                    self.lista_traco[t] = letra
            self.msg['text'] = ' '.join(self.lista_traco)
        else:
            self.lista_erro.append(letra)
            self.msg2['text'] = 'Letras Erradas: ' + ' '.join(self.lista_erro)

        self.caixa.set('')

        if set(self.digito) == set(self.lista_letras):
            self.msg3['text'] = 'Jogo ganho, parabéns!'
            self.msg3['fg'] = 'green'

        if len(self.lista_erro) == 10:
            self.msg3['text'] = '10 erros, você perdeu!'
            self.msg3['fg'] = 'red'
            self.nom.destroy()

    def sair(self):
        self.root.destroy()

    def novo(self):
        self.root.destroy()
        new_root = Tk()
        JogoDaForca(new_root)

def main():
    janela = Tk()
    jogo = JogoDaForca(janela)
    janela.protocol("WM_DELETE_WINDOW", jogo.sair)
    janela.mainloop()

if __name__ == "__main__":
    main()
