import pygame
from pygame.locals import *

class Posicao:
    def __init__(self, x=-1, y=-1, valor=0, estado=False, xmax=8, ymax=8, exposto=False, mostra=True):
        # Atributos
        self.X = x
        self.Y = y
        self.Valor = valor
        self.Estado = estado
        self.Xmax = xmax
        self.Ymax = ymax
        self.Exposto = exposto
        self.Botao = 0
        self.PaltLefet = [0, 0]

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
        return self.Ymax

    def getExposto(self):
        return self.Exposto

    def setX(self, x):
        self.X = x

    def setY(self, y):
        self.Y = y

    def setValor(self, v):
        """-1 = bombomba, podendo ir ate 8"""
        self.Valor = v

    def setEstado(self, e):
        """True/False"""
        self.Estado = e

    def setExposto(self, t):
        """True/False"""
        self.Exposto = t

    # metodos especifcos
    def RecebeBomba(self):
        self.Valor = -1

    def marcar(self):
        self.Estado = not self.Estado

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

    def lados(self, campos, used = []):
        from Cod import nomeador

        nomes = []
        x = self.X
        y = self.Y
        Xmax = self.Xmax
        Ymax = self.Ymax
        campos2 = []

        for vx in range(x - 1, x + 2):
            if 0 < vx <= Xmax:
                for vy in range(y - 1, y + 2):
                    if 0 < vy <= Ymax:
                        nome = [vx, vy]
                        if nome not in used:
                            nomes.append(nome)
        for nome in nomes:
            campo = campos[nome[0]-1][nome[1]-1]
            campos2.append(campo)

        return campos2

    def aredores(self, campos):
        if self.Valor != -1:
            nomes = self.lados(campos)
            for nome in nomes:
                if nome.Valor == -1:
                    self.Valor += 1

    def respostas(self):
        var = self.Valor
        if self.Estado:
            if var == 0:
                self.varedura()

            elif var > 0:
                self.Exposto = True

            elif var == -1:
                fim = self.esplodir()
        else:
            print('estar marcado')

    def varedura(self, campos, used):
        exibir = []

        ared = self.lados(campos)
        for v in ared:
            beta = v.lados(campos, used)
            for c in beta:
                if not c.Estado:
                    if c.Valor == 0:
                        c.Estado = True
                        cod = [c.X-1, c.Y-1]
                        used.append(cod)
                        ared.append(c)
                    elif c.Valor != -1:
                        c.Estado = True


        return used

    def iterface(self, tela):
        pos = (self.X, self.Y)
        class Bandeira(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.icone = pygame.image.load('bandeira.png')
                self.rect = self.icone.get_rect()
                self.rect.topleft = pos[0], pos[1]


        band = Bandeira()
        bandeira = pygame.sprite.Group()
        bandeira.add(band)
        bandeira.draw(tela)
        bandeira.update()
        return bandeira
    pass
