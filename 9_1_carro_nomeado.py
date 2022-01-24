# Desafio 9.1 - Desafio do Carro Nomeado
# Criar uma classe Carro onde além de estado também tem um nome por padrão (Construtor).
# Criar um método nessa classe Carro onde vai printar para gente o Nome e o Estado do carro.

class Carro(object):
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def printar(self):
        return print(f"O carro {self.nome} tem o estado {self.estado}.")

fusca = Carro('Fusca', 'usado')
lada = Carro('Lada', 'único dono')
brasilia = Carro('Brasília', 'querado')

fusca.printar()
lada.printar()
brasilia.printar()
