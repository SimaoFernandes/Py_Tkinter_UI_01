from tkinter import *
import random
import process

vitorias, empates, derrotas = 0, 0, 0

def sair(root):
    root.quit()

def printresultado(root, userInput):
    ppt=['pedra','papel','tesoura']
    choice = random.choice(ppt)
    uInput = getInput(userInput)
    global l , ws, ls, ds, vitorias, empates, derrotas
    text = process.process(uInput, choice)

    Resultado['text'] = text
    if text == 'Ganhou':
        vitorias += 1
        ws['text'] = f'{vitorias}'
    if text == 'Perdeu':
        derrotas += 1
        ls['text'] = f'{derrotas}'
    if text == 'Empate':
        empates += 1
        ds['text'] = f'{empates}'

def getInput(userInput):
    return userInput.get().lower().strip()

root = Tk()
root.title('Pedra Papel Tesoura')

Titulo = Label(root, text=f'Pedra Papel ou Tesoura')
Titulo.grid(column = 1 , row = 0)

userInput = Entry(root, width = 38)
userInput.grid(column = 1 , row = 1)

white = Label(root, text = ' ')
white.grid(column = 1 , row = 2)

submitButton = Button(root,text= 'Jogar', command = lambda: printresultado(root,userInput))
submitButton.grid(column = 1 , row = 3)

Resultado = Label(root, text = ' ')
Resultado.grid(column = 1 , row = 4)

w = Label(root, text = 'Vitoria')
ws = Label(root, text = '0')
w.grid(column = 0, row = 5)
ws.grid(column = 0, row = 6)

l = Label(root, text = 'Derrota')
ls = Label(root, text = '0')
l.grid(column = 1, row = 5)
ls.grid(column = 1, row = 6)

d = Label(root, text = 'Empate')
ds = Label(root, text = '0')
d.grid(column = 2, row = 5)
ds.grid(column = 2, row = 6)

white = Label(root, text = ' ')
white.grid(column = 0 , row = 7)

exitButton = Button(root,text= 'Sair', command = lambda:sair(root))
exitButton.grid(column = 1 , row = 8)

root.grid_columnconfigure(0, minsize=30)
root.grid_columnconfigure(1, minsize=100)
root.grid_columnconfigure(2, minsize=30)

root.mainloop()