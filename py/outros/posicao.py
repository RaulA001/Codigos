class Posicao:
    def __init__(self, x=-1, y=-1, valor=0, estado=False, xmax = 8, ymax = 8, exposto = False):
        # Atributos
        self.X = x
        self.Y = y
        self.Valor = valor
        self.Estado = estado
        self.Xmax = xmax
        self.Ymax = ymax
        self.Exposto = exposto

    # metosdos set/get
    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getValor(self):
        return self.Valor

    def getEstado(self):
        return self.Estado

    def getXmax(self):
        return self.Xmax

    def getYmax(self):
        return  self.Ymax

    def getExposto(self):
        return self.Exposto

    def setX(self, x):
        self.X = x

    def setY(self, y):
        self.Y = y

    def setValor(self, v):
        '''-1 = bombomba, podendo ir ate 8'''
        self.Valor = v

    def setEstado(self, e):
        '''True/False'''
        self.Estado = e

    def setExposto(self, t):
        '''True/False'''
        self.Exposto = t

    # metodos especifcos
    def RecebeBomba(self):
        self.Valor = -1

    def marcar(self):
        if self.Estado:
            self.Estado = False
        elif not self.Estado:
            self.Estado = True

    def esplodir(self):
        if self.Valor == 0 and self.Estado:
            print('Esplodio')
            return "0voce perdeu"

    def Mostra_Status(self, retorna=False):
        x = self.X
        y = self.Y
        e = self.Estado
        ex = self.Exposto

        if e:
            res = 'Ativa'
        else:
            res = 'Desativada'
        if ex:
            mos = 'aparecendo'
        else:
            mos = 'não esta aparecendo'

        if not retorna:
            print(f'''pos = {x},{y}
            esta {res}, é {mos}''')

        else:
            lista = (x, y, e)
            return lista

    def lados(self):
        from Cod import nomeador

        nomes = []
        x = self.X
        y = self.Y
        Xmax = self.Xmax
        Ymax = self.Ymax

        for vx in range(x - 1, x + 2):
            if 0 < vx < Xmax:
                for vy in range(y - 1, y + 2):
                    if 0 < vy < Ymax:
                        nome = nomeador(vx, vy)
                        nomes.append(nome)
        return nomes


    def aredores(self,):
        if self.Valor != -1:
            nomes = self.lados()
            for nome in nomes:
                if nome.Valor == -1:
                    self.Valor += 1

    def respostas(self):
        var = self.Valor
        if self.Estado:
            if var == 0:
                achadas = self.varedura()

            elif var > 0:
                self.Exposto = True

            elif var == -1:
               fim = self.esplodir()
        else:
            print('estar marcado')

    def varedura(self):
        exibir = []
        lados1 = self.lados()
        for lado1 in lados1:
            if not lado1.Exposto:
                exibir.append(lado1)
                lados2 = lado1.lados()
                for lado2 in lados2:
                    if not lado2.Exposto and lado2.Valor == 0:
                        lados1 = lado2.lados()
        for nome in exibir:
            nome.setExposto(True)


    pass
