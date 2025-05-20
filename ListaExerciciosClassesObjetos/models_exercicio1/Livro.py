class Livro:
    
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_pubblicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self):

        if self.pagina_atual < 576:
            self.pagina_atual += 1
        
    def voltar_pagina(self):
        
        if self.pagina_atual > 0:
            self.pagina_atual -= 1

    def exibir_informacoes(self):

        print(
            f'As iformações atuais sobre o livro são: \n TÍTULO: {self.titulo} \n AUTOR: {self.autor} \n ANO DE PULICAÇÃO: {self.ano_pubblicacao} \n N° PÁGINAS: {self.numero_paginas} \n PÁGINA ATUAL: {self.pagina_atual}'
        )
