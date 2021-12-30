import pygame

from janela import Janela
from posicao import Posicao
from Cod import *


class Play(Janela, Posicao):
    def __init__(self, nome='💓Caça mina simuleitor💓', resolucao=1, dt=[8, 8, 8], x=-1, y=-1, valor=0, estado=False,
                 xmax=8, ymax=8, exposto=False):
        Janela.__init__(self, nome, resolucao, dt)
        Posicao.__init__(self, x, y, valor, estado, xmax, ymax, exposto)
        self.muda = []
        self.mostre = False
        self.conf_bots = []
        self.botoes = []
        self.cods = []
        self.codsb = []
        self.botoesb = []
        self.VD = [False, False]
        self.Nuns = []
        self.Used = []
        self.pos = []
        self.OK = False
        self.fonte = 'n'
        self.fonte1 = 'n'
        self.bomb = 'n'
        self.band = 'n'
        self.band1 = 'n'
        self.notrept = []

    def PrintPlay(self):
        pygame.init()

        while True:
            self.Tela = Janela(self.Nome, self.NUM_Res, self.Dados)

            # cores
            cor_toque = (34, 139, 34)

            # cordenadas
            mxy = self.Tela.Mxy
            pos = self.Tela.Resolucao
            lag = pos[0]
            alt = pos[1]

            self.fonte = pygame.font.SysFont("arial", int((alt * 0.07) * 0.75), True, False)
            alt2 = alt/self.Ymax
            self.fonte1 = pygame.font.SysFont("arial", int((alt * 0.07) * 0.75), True, False)
            ban = pygame.image.load('bandeira.png')
            ban.convert(self.Tela.Tela)
            ban = pygame.transform.scale(ban, (int(alt * 0.08), int(alt * 0.08)))
            self.band = ban
            self.band1 = ban

            bom = pygame.image.load('Mina.png')
            bom.convert(self.Tela.Tela)
            self.bomb = bom

            campos = self.Ant_buld_sp()

            tempo = pygame.time.Clock()

            while True:
                self.Tela.Def_Mxy()
                tempo.tick(10)
                self.Tela.Tela.fill((85,107,47))

                num_bom_free = self.Dados[0]

                barra = pygame.draw.rect(self.Tela.Tela, (158, 225, 68), (0, 0, lag, alt * 0.08))
                det = pygame.draw.rect(self.Tela.Tela, (158, 225, 68),
                                             (lag - alt * 0.08, 0, alt * 0.08, alt * 0.08))

                self.Criar_botoes(campos, det)

                self.Opem_Configu()

                for acao in pygame.event.get():
                    self.Tela.fechar(acao)

                    if self.mosuse(acao, 1, 0, True):
                        if det.collidepoint(mxy[0], mxy[1]):
                            self.mostre = not self.mostre

                num_bom_free -= len(self.botoes)
                text_num = self.fonte.render(f'{num_bom_free}', True, (0, 0, 0))
                self.Tela.Tela.blit(text_num, (int(alt * 0.10), alt*0.01))

                self.Tela.Tela.blit(self.band1, (0, 0))

                inc = pygame.image.load('Incone_config.png')
                inc.convert(self.Tela.Tela)
                inc = pygame.transform.scale(inc, (int(alt * 0.08), int(alt * 0.08)))
                self.Tela.Tela.blit(inc, (lag-alt*0.08, 0))

                #self.Vitoria_Derota()

                #print(self.Used)
                pygame.display.update()


    def Criar_botoes(self, campos, det):
        xm = self.Xmax
        ym = self.Ymax
        pos = self.Tela.Resolucao
        lag = pos[0]
        alt = pos[1]
        mxy = self.Tela.Mxy

        larg = int(alt * 0.88 / ym)
        altu = int(alt * 0.88 / ym)

        if larg*xm > lag*0.9333:
            larg = int((lag * 0.955) / xm)

        for x in range(1, xm + 1):

            if x == 1:
                espasoX = (lag - larg*self.Xmax)/2

            else:
                espasoX += larg

            for y in range(1, ym + 1):

                if y == 1:
                    espasoY = alt * 0.1
                else:
                    espasoY += altu

                if (y + x%2)%2 == 0:
                    cor = (173, 255, 47)
                    if campos[x - 1][y - 1].Estado:
                        cor = (255, 222, 173)
                else:
                    cor = (154, 205, 50)
                    if campos[x - 1][y - 1].Estado:
                        cor = (222, 184, 135)

                nome =pygame.draw.rect(self.Tela.Tela, cor,
                                       (espasoX, espasoY, larg, altu))

                if not self.mostre:
                    for bots in self.botoes:
                        self.Tela.Tela.blit(bots[0], bots[1])

                    for botsb in self.botoesb:
                        self.Tela.Tela.blit(botsb[0], botsb[1])

                if self.Estado:
                    cod = [x - 1, y - 1]
                    self.Used.append(cod)

                if nome.collidepoint(mxy[0], mxy[1]) or self.mostre:

                    if (y + x % 2) % 2 == 0:
                        cor = (173, 255, 47)
                        if campos[x - 1][y - 1].Estado:
                            cor = (255, 222, 173)
                    else:
                        cor = (154, 205, 50)
                        if campos[x - 1][y - 1].Estado:
                            cor = (222, 184, 135)

                    campos[x-1][y-1].Botao = pygame.draw.rect(self.Tela.Tela, cor,
                                            (espasoX, espasoY, larg, altu))

                    for event in pygame.event.get():
                        self.Tela.fechar(event)

                        if self.mosuse(event, 1, campos[x-1][y-1].Botao, True):
                            if self.mostre:
                                if self.conf_bots[0].collidepoint(mxy[0], mxy[1]):
                                    self.mostre = False

                                if self.conf_bots[1].collidepoint(mxy[0], mxy[1]):
                                    self.mostre = False

                                if self.conf_bots[2].collidepoint(mxy[0], mxy[1]):
                                    self.mostre = False

                            if det.collidepoint(mxy[0], mxy[1]):
                                self.mostre = not self.mostre
                                campos[x - 1][y - 1].Botao = pygame.draw.rect(self.Tela.Tela, cor,
                                                                              (espasoX, espasoY, larg, altu))

                            if campos[x-1][y-1].Botao.collidepoint(mxy[0], mxy[1]):
                                if campos[x - 1][y - 1].Exposto:
                                    campos[x - 1][y - 1].Estado = True
                                    if campos[x - 1][y - 1].Valor == -1:

                                        self.bomb = pygame.transform.scale(self.bomb, (larg, altu))
                                        rectb = self.bomb.get_rect()
                                        rectb.topleft = espasoX, espasoY

                                        lis = [self.bomb, rectb]

                                        if self.botoesb == []:

                                            self.botoesb.append(lis)

                                        if not [x, y] in self.notrept:
                                            self.notrept.append([x, y])
                                            self.botoesb.append(lis)

                                        if len(self.botoesb) == 1:
                                            som_bomba = self.Tela.Imp_Son('Boom.wav', 100)
                                            som_bomba.play(0)


                                        self.VD[1] = True
                                    elif campos[x - 1][y - 1].Valor == 0:

                                        ared = campos[x - 1][y - 1].lados(campos, self.Used)
                                        for v in ared:
                                            beta = v.lados(campos, self.Used)
                                            for c in beta:
                                                if not c.Estado:
                                                    if c.Valor == 0:
                                                        c.Estado = True
                                                        cod = [c.X - 1, c.Y - 1]
                                                        self.Used.append(cod)
                                                        ared.append(c)
                                                    elif c.Valor != -1:
                                                        c.Estado = True

                                    elif campos[x - 1][y - 1].Valor > 0:
                                        cod = [x - 1, y - 1]
                                        self.Used.append(cod)
                                        campos[x - 1][y - 1].Estado = True

                        elif self.mosuse(event, 3, campos[x-1][y-1].Botao, True):
                            if not campos[x - 1][y - 1].Estado:
                                campos[x-1][y-1].Exposto = not campos[x-1][y-1].Exposto

                                self.band = pygame.transform.scale(self.band, (larg, altu))
                                rect = self.band.get_rect()
                                rect.topleft = espasoX, espasoY

                                cod = f'sps {x}, {y}'
                                lis = [self.band, rect]

                                if not campos[x-1][y-1].Exposto:
                                    if not cod in self.cods:
                                         self.cods.append(cod)
                                         self.botoes.append(lis)
                                else:
                                    if cod in self.cods:
                                        self.botoes.pop(self.cods.index(cod))
                                        self.cods.remove(cod)

                if campos[x - 1][y - 1].Estado and campos[x - 1][y - 1].Valor > 0:
                    text = f'{campos[x - 1][y - 1].Valor}'
                    text_num = self.fonte1.render(text, True, (0, 0, 0))
                    self.Tela.Tela.blit(text_num, (espasoX + larg*0.35, espasoY + altu*0.19))
        #casso der erro colocar self.botoes = []


    def Ant_buld_sp(self):
        xm = self.Xmax
        ym = self.Ymax

        from random import randint
        cod = []
        for n in range(0, self.Dados[0]):
            x = randint(1, self.Xmax)
            y = randint(1, self.Ymax)
            pos = [x, y]
            if pos in cod:
                n -= 1
            cod.append(pos)

        campos = []
        for x in range(1, xm + 1):

            camp = []
            for y in range(1, ym + 1):

                nomed = nomeador(x, y, 0)
                if [x, y] in cod:
                    nomed= Posicao(x, y, -1, False, xm, ym, True, False)
                else:
                    nomed = Posicao(x, y, 0, False, xm, ym, True, False)

                camp.append(nomed)
            campos.append(camp)
        for x in range(1, xm + 1):
            for y in range(1, ym + 1):
                campos[x-1][y-1].aredores(campos)

        return campos

    def Opem_Configu(self):
        if self.mostre:
            mxy = self.Tela.Mxy
            pos = self.Tela.Resolucao
            lag = pos[0]
            alt = pos[1]

            text_Volta = self.fonte.render('Volta', True, (0, 0, 0))
            text_Reiniciar = self.fonte.render('Reiniciar', True, (0, 0, 0))
            text_Menu = self.fonte.render('Menu', True, (0, 0, 0))

            fund = pygame.draw.rect(self.Tela.Tela, (152, 251, 152),
                                    (0, alt * 0.2, lag, alt * 0.6))

            cor = []
            for c in range(0, 4):
                cor.append((255, 160, 122))

            for v in self.muda:
                cor.insert(v, (205, 100, 102))

            self.muda = []

            Bres1 = pygame.draw.rect(self.Tela.Tela, cor[1], (lag * 0.35, alt * 0.25, lag * 0.3, alt * 0.10), 0, 50)
            if Bres1.collidepoint(mxy[0], mxy[1]):
                self.muda.append(1)

            self.Tela.Tela.blit(text_Volta, (lag * 0.466, alt * 0.27))

            Bres2 = pygame.draw.rect(self.Tela.Tela, cor[2], (lag * 0.35, alt * 0.45, lag * 0.3, alt * 0.10), 0, 50)
            if Bres2.collidepoint(mxy[0], mxy[1]):
                self.muda.append(2)

            self.Tela.Tela.blit(text_Reiniciar, (lag * 0.44, alt * 0.47))

            Bres3 = pygame.draw.rect(self.Tela.Tela, cor[3], (lag * 0.35, alt * 0.65, lag * 0.3, alt * 0.10), 0, 50)
            if Bres3.collidepoint(mxy[0], mxy[1]):
                self.muda.append(3)

            self.Tela.Tela.blit(text_Menu, (lag * 0.46, alt * 0.67))

            self.conf_bots = [Bres1, Bres2, Bres3]

    def Vitoria_Derota(self):
        if self.VD[0]:
            print('Vitoria')
        elif self.VD[1]:
            print('derrota')









#    def Pos_bombas(self):
#        from random import randint
#        cod = []
#        for bom in (0, self.Dados[0]):
#            x = randint(0, self.Xmax)
#            y = randint(0, self.Ymax)
#            pos = (x, y)
#            cod.append(pos)
#        return cod

jogo = Play()
jogo.PrintPlay()
#jogo.Ant_buld_sp()

#cu = ['als', 'ds']
#cuu = ['ds']
#if cuu[0] in cu:
#    print('caralho')