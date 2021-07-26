'''
Você deverá criar um programa para o gerenciamento de uma loja de livros, CDs
e DVDs. Para tanto, você deve:
• Criar uma classe Produto que tem como atributos: Titulo, Valor e Desconto, e o
método descreve_produto, que mostra todas as informações do produto;

'''

class Produto():
    def __init___(self):
        self.titulo = None
        self.valor = 0
        self.desconto = 1
        self.desc_Prod = None

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor * self.getDesconto()

    def getDesconto(self):
        return self.desconto

    def setDesconto(self, desconto):
        self.desconto = desconto

    def descreve_produto(self, desc_Prod):
        self.desc_Prod = desc_Prod

'''
• Criar uma classe Livro que herda de Produto e tem o atributo Autor e o método
descreve_produto, que mostra todas as informações do livro;

'''

class Livro(Produto):
    def __init__(self):
        super().__init__()
        self.autor = None
          
    def getDesconto(self):
        return self.desconto * 0.9

    def descreve_produto(self, desc_Prod):
        self.desc_Prod = desc_Prod

'''
• Criar uma classe CD que herda de Produto e tem o atributo Artista e o método
descreve_produto, que mostra todas as informações do CD;
'''

class CD(Produto):
    def __init__(self):
        super().__init__()
        self.artista = None
        
    def getDesconto(self):
        return self.desconto * 0.85

    def descreve_produto(self, desc_Prod):
        self.desc_Prod = desc_Prod

'''
• Criar uma classe DVD que herda de Produto e tem o atributo Duração e o método
descreve_produto, que mostra todas as informações do DVD;
'''
class DVD(Produto):
    def __init__(self):
        super().__init__()
        self.duracao = None

    def getDesconto(self):
        return self.desconto * 0.8
        
    def descreve_produto(self, desc_Prod):
        self.desc_Prod = desc_Prod
'''
• Por padrão, todos os livros tem 10% de desconto, todos os CDs tem 15% de
desconto e os DVDs tem 20% de desconto, referente ao preço base;
'''

'''
• Você deve criar vários objetos do tipo Produto, Livro, CD e DVD e adicioná-los
a uma lista de produtos. Depois, você deve percorrer a lista para pegar o valor do
produto (com desconto, se for o caso) e soma-los para obter um total.
'''

obj_Livro = Livro()
obj_CD = CD()
obj_DVD = DVD()