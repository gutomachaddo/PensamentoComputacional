'''
import tkinter as tk

status = 0

def imprimirInfos():
    global status
    texto = ['Mundo', 'Turma']
    rotulo.config(text='Olá, '+ texto[status])
    status = not status

janela  = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text= "Clique no botão abaixo!", font=("Arial", 16))
rotulo.pack(pady= 10)
botao = tk.Button(janela, text="Clique aqui", command=imprimirInfos)
botao.pack(pady= 10)
janela.mainloop()
'''
import tkinter as tk

class objeto():
    valor = 0

def ImprimirInfos():
    objeto.valor += 1
    if objeto.valor == 1:
        rotulo.config(text='Olá, mundo!')
    
    else:
        rotulo.config(text='Olá, turma!')
        objeto.valor -= 1
            
janela  = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text= "Clique no botão abaixo!", font=("Arial", 16))
rotulo.pack(pady= 10)
botao = tk.Button(janela, text="Clique aqui", command=ImprimirInfos)
botao.pack(pady= 10)
janela.mainloop()