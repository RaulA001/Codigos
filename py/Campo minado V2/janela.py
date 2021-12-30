from Met_janela import *
import pygame
from pygame.locals import *
from sys import exit


class Janela:
    pygame.init()
    def __init__(self, nome='💓Caça mina simuleitor💓', resolucao=1, dt=[6, 8, 8]):
        self.Nome = nome
        self.NUM_Res = resolucao
        pygame.display.set_caption(self.Nome)
        self.Resolucao = deCodRes(resolucao)
        self.Songs = []
        self.Imagens = []
        self.Tela = pygame.display.set_mode(self.Resolucao)
        self.Mxy = [0, 0]
        self.Dados = dt

    def Imp_Botao(self, n=0):
        return pygame.draw.rect(self.Tela, self.Botoes[n][1], self.Botoes[n][2], self.Botoes[n][3], self.Botoes[n][4])

    def Def_Mxy(self):
        mx, my = pygame.mouse.get_pos()
        self.Mxy[0] = mx
        self.Mxy[1] = my

    def Imp_Son(self, lacais, volume, salvar = True):
        som =pygame.mixer.Sound(lacais)
        som.set_volume(volume)
        if salvar:
            self.Songs.append(som)
        return som

    def Imp_Imagens(self, lacais, scala=False):
        imagem = pygame.image.load(lacais)
        if scala:
            imagem = pygame.transform.scale(imagem, (self.Resolucao[0], self.Resolucao[1]))

        return imagem

    def fechar(self, acao):
        ok = False
        if acao != True:
            if acao.type == QUIT:
                ok = True
        elif acao == True:
                ok = True
        if ok:
            pygame.quit()
            exit()

    def mosuse(self, acao, n, obj, simples):
        r = False
        if acao.type == MOUSEBUTTONDOWN:
            if acao.button == n:
                if simples:
                    r = True
                else:
                    mxy = self.Mxy
                    if obj.collidepoint(mxy[0], mxy[1]):
                        r = True
        return r



#    def Inc_texto(self, font, N_fonte=0, N_texto=0, N_botoes=0, TPPalt=0.75, TPPlag=0.9):
#        cod = self.Resolucao
#        lag = cod[0]
#        alt = cod[1]
#
#        bot = self.Botoes[N_botoes]
#        bx = bot[2][2]
#        by = bot[2][3]
#
#        tx = self.Textos[N_texto]
#        text = font.render('Caça mina simuleitor', True, (255, 0, 0))
#
#        tamanho = self.Fonte[N_fonte][0][1]
#
#        botão = pygame.draw.rect(self.Tela, bot[1], bot[2], bot[3], bot[4])
#        Xx = (lag * bx - tamanho * TPPlag) / 2
#        XX = int((Xx / (lag / 100))+bot[2][0])
#
#        Yy = (alt * by - tamanho * TPPalt)
#        YY = int((Yy / (alt / 100))+bot[2][1])
#
#        return (text, (XX, YY))
#
#    def Imp_fonte(self, N_fonte=0, N_botoes=0, esp0=0.03, esp1=0.05, TPPalt=0.75, TPPlag=0.9, ussarBx=True, ussarBY=True):
#        cod = self.Resolucao
#        lag = cod[0]
#        alt = cod[1]
#
#        bot = self.Botoes[N_botoes]
#        bx = bot[2][2]
#        by = bot[2][3]
#
#        fon = self.Fonte[N_fonte][0]
#        if ussarBY:
#            tam1 = (alt * (by - esp0) * TPPalt)
#            tamanho = tam1
#
#        if ussarBx:
#            tam2 = (lag * (bx - esp1) * TPPlag)
#            tamanho = tam2
#
#        if ussarBY and ussarBx:
#            tamanho = int((tam1 + tam2) / 2)
#
#        self.Fonte.insert(N_fonte+1, (fon[0], tamanho, fon[2], fon[3]))
#        self.Fonte.pop(N_fonte)
#        fon = self.Fonte[N_fonte]





#    def movimento(self):
#        if pygame.key.get_pressed()[K_a]:
#            x -= vel
#        if pygame.key.get_pressed()[K_d]:
#            x += vel
#
#        if pygame.key.get_pressed()[K_w]:
#            y -= vely
#        if pygame.key.get_pressed()[K_s]:
#            y += vely
#
#        pos = [x, y]
#        return pos

    # em outra def Movimento(self):