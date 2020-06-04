class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == '__main__':
    joao = Pessoa(nome='João')
    anselmo = Pessoa(joao, nome='Anselmo')
    print(Pessoa.cumprimentar(anselmo))
    print(id(joao))
    print(anselmo.cumprimentar())
    print(anselmo.nome)
    print(joao.idade)
    for filho in anselmo.filhos:
        print(filho.nome)
    anselmo.sobrenome = 'Marques'
    del anselmo.filhos
    print(anselmo.__dict__)
    print(joao.__dict__)
