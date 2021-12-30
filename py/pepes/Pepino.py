class Plata():
    def __init__(self, fruto, corpo, nutrites):

        self.Frut = fruto
        self.Cop = corpo
        self.Nut = nutrites

    def crecer(self, corpo, n, a):
        self.Cop = corpo
        self.Nut = n
        self.Frut = a
        print(self.Cop, self.Nut, self.Frut)

    pass

pep = Plata(2, 1, 3)
pep.crecer(3, 2, 1)
print('\n', '/--$--'*80, '\n')

class Pepino(Plata):
    def __init__(self, fruto, corpo, nutrites):

        super(Pepino, self).__init__(fruto, corpo, nutrites)

lapepe = Pepino(1, 2, 3)
lapepe.crecer(1, 2, 3)
