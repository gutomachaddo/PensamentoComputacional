import tkinter as tk

status = 0

def imprimirInfos():
    global status
    texto = ['Mundo', 'Turma']
    rotulo.config(text='Olá, '+ texto[status])
    status = not status
'''
def Imprimir2():
    rotulo.config(text = "Olá turma!")
'''


janela  = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text= "Clique no botão abaixo!", font=("Arial", 16))
rotulo.pack(pady= 10)
botao = tk.Button(janela, text="Clique aqui")
botao = tk.Button(janela, text="Clique aqui", command=imprimirInfos)
botao.pack(pady= 10)
janela.mainloop()