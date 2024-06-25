class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def exibirInformações(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("Ano: ", self.ano)
        

livro1 = Livro("A volta ao munod em 80 dias", "Julio Verne", 2008)
livro1.exibirInformações()