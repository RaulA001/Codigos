class Bomba:
    def __init__(self, x=-1, y=-1, ativa=False):
        self.X = x
        self.Y = y
        self.Ativa = ativa

    # Get/Set

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getAtiva(self):
        return self.Ativa

    def setX(self, x):
        if x > 0:
            self.X = int(x)

    def setY(self, y):
        if y > 0:
            self.Y = y

    def setAtiva(self, a):
        self.Ativa = bool(a)

    # funçoes

    def iniciar(self, xmax, ymax, num):
        from random import randint
        for x in range(0, num)
        x = randint(0, xmax)
        y = randint(0, ymax)
        self.setX(x)
        self.setY(y)

    def marca(self, x, y):
        from Cod import xy
        posc = xy(x, y)
        posb = xy(self.X, self.Y)
        if posc == posb:
            print('Marcada')
            self.setAtiva(True)

    def esplodir(self, x, y):
        from Cod import xy
        posc = xy(x, y)
        posb = xy(self.X, self.Y)
        if self.Ativa is False and posc == posb:
            print('Esplodio')
            return "0voce perdeu"

    def estado(self, retorna=False):
        x = self.X
        y = self.Y
        e = self.Ativa

        if e:
            res = 'Ativa'
        else:
            res = 'Desativada'

        print(f'''pos = {x},{y}
{res}''')

        if retorna:
            lista = (x, y, e)
            return lista

    pass
