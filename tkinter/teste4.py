import tkinter as tk

def mostrar_opcao(botao):
    rotulo.config(text = f'Escolheu: {botao}')

    if opcao1.get() and opcao2.get(): # funciona
        if botao == 'saúde':
            opcao1.set(False)
            
    if opcao2.get() and opcao3.get():
        if botao == 'dinheiro':
            opcao2.set(False)

    if opcao1.get() and opcao3.get(): # funciona
        if botao == 'tempo':
            opcao3.set(False)

janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")

opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()


tk.Radiobutton(janela, text="Dinheiro", variable=opcao1, value=True, command= lambda: mostrar_opcao('dinheiro')).pack()
tk.Radiobutton(janela, text="Tempo", variable=opcao2, value=True, command= lambda: mostrar_opcao('tempo')).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command= lambda: mostrar_opcao('saúde')).pack()
rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()