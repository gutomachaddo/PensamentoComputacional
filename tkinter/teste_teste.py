import tkinter as tk
from tkinter import messagebox

def botao_clicado(nome_botao):
    """
    Função que é executada quando um botão é clicado.
    Recebe o nome do botão como argumento.
    """
    messagebox.showinfo("Botão Clicado", f"Você clicou no botão: {nome_botao}")
    # Aqui você pode adicionar a lógica para lidar com o botão clicado

janela = tk.Tk()
janela.title("Exemplo com Múltiplos Botões")

nomes_botões = ["Botão 1", "Botão 2", "Botão 3"]

# Cria uma lista de botões e associa a função ao evento de clique
for nome in nomes_botões:
    botao = tk.Button(janela, text=nome, command=lambda n=nome: botao_clicado(n))  # Usa lambda para passar o nome do botão
    botao.pack(pady=10)

janela.mainloop()