class pessoa:
    def __init__(self, nome, sexo, nacimento):
        self.nome = nome
        self.sexo = sexo
        self.data = nacimento
        self.anos = 2000

    def anivesario(self):
        print(self.data[3:5])
        v = self.data[3:5]
        if 10 - int(v) == 0:
            if 3 - self.data[:3] ==0:
                self.anos += 1

    pass

class puta(pessoa):
    def __init__(self, nome, sexo, nacimento):
        pessoa.__init__(self, nome, sexo, nacimento)
        self.valida = "0"

    @classmethod
    def validação(self):
        self.anos > 17

    def status(self):
        print(f'''{self.nome} tem {self.anos}, logo é {self.valida}
        ela faz anivesario em {self.data} tarzer prezentes :3''')

macia = puta('Marcia', 'F', '12/03/2000')
macia.status()
macia.anivesario()
macia.status()

