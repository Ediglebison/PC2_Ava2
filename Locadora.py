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
        self.produtos = []

    def getProdutos(self):
        return self.produtos

    def setProdutos(self, produtos):
        self.produtos = produtos

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getValor(self):
        valor_final = self.valor * self.getDesconto()
        return valor_final

    def setValor(self, valor):
        self.valor = valor

    def getDesconto(self):
        return self.desconto

    def setDesconto(self, desconto):
        self.desconto = desconto

    def descricao(self):
        return self.desc_Prod

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

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor
          
    def getDesconto(self):
        desc = super().desconto * 0.9
        return desc

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

    def getArtista(self):
        return self.artista

    def setArtista(self, artista):
        self.artista = artista
        
    def getDesconto(self):
        desc = super().desconto * 0.85
        return desc

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

    def getDuracao(self):
        return self.duracao

    def setDuracao(self, duracao):
        self.duracao = duracao

    def getDesconto(self):
        desc = super().desconto * 0.8
        return desc
        
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

obj_Produto = Produto()
obj_Livro = Livro()
obj_CD = CD()
obj_DVD = DVD()

obj_Produto.setTitulo("Café")
obj_Produto.setValor(3.00)
obj_Produto.descreve_produto("Produto muito utilizado por programadores em seu dia a dia")
obj_Produto.setDesconto(1)

obj_Livro.setTitulo("Redes de Computadores")
obj_Livro.setValor(149.90)
obj_Livro.descreve_produto("´Redes de computadores´ foi atualizado para refletir as tecnologias mais novas e \
                            mais importantes de redes, com ênfase especial em redes sem fio, incluindo 802.11, \
                            Bluetooth, comunicação sem fio de banda larga, redes ad hoc, i-mode e WAP. Porém, \
                            as redes fixas não foram ignoradas com cobertura de ADSL, Internet via cabo, Ethernet \
                            de gigabit, redes não-hierárquicas, NAT e MPLS.")
obj_Livro.setAutor("Andrew Tanenbaum")
obj_Livro.setDesconto(1)

obj_CD.setTitulo("CD - Coletanea programação")
obj_CD.setValor(20)
obj_CD.descreve_produto("Musicas para ouvir enquanto programa")
obj_CD.setArtista("Artistas desconhecidos")
obj_CD.setDesconto(1)

obj_DVD.setTitulo("DVD - Coletanea Clipes programação")
obj_DVD.setValor(20)
obj_DVD.descreve_produto("Clipes para Assistir apos programar")
obj_DVD.setDuracao("Artistas desconhecidos")
obj_DVD.setDesconto(1)

    
produto1 = [obj_Produto.getTitulo(), obj_Produto.descricao(), obj_Produto.getValor()]
produto2 = [obj_Livro.getTitulo(), obj_Livro.descricao(), obj_Livro.getAutor(), obj_Livro.getValor()]
produto3 = [obj_CD.getTitulo(), obj_CD.descricao(), obj_CD.getArtista(), obj_CD.getValor()]
produto4 = [obj_DVD.getTitulo(), obj_DVD.descricao(), obj_DVD.getDuracao(), obj_DVD.getValor()]

print (produto1)
print (produto2)
print (produto3)
print (produto4)