class Pessoa:

    def __init__(self, id):
        self.id = id
        self.idade = 0
        self.nome = ""

    def set_idade(self, idade):
        self.idade = idade * 2

    def set_nome(self, nome):
        self.nome = nome
