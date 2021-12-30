from janela import *
from Menu_Configuracao import MenuConfiguracao


class MainMenu(Janela):
    def __init__(self, nome='💓Caça mina simuleitor💓', resolucao = 1, dt=[[6, 8, 8]]):
        super().__init__(nome, resolucao, dt)

    def Print_Main_menu(self):

        pygame.init()

        self.Tela = Janela(self.Nome, self.NUM_Res)

        # midia
        fundo = self.Tela.Imp_Imagens('fundo.gif', True)

        # cores
        cor_toque = (240, 128, 128)
        muda = []

        # cordenadas
        mxy = self.Tela.Mxy
        pos = self.Tela.Resolucao
        lag = pos[0]
        alt = pos[1]

        # Fontes
        fonte = pygame.font.SysFont("arial", int((alt * 0.07) * 0.75), True, False)
        fonte1 = pygame.font.SysFont("arial", int((alt * 0.055) * 0.75), True, False)
        fonte2 = pygame.font.SysFont("arial", int((alt * 0.13) * 0.75), True, True)
        fonte3 = pygame.font.SysFont("arial", int((alt * 0.03) * 0.75), True, False)

        # Textos
        cor_text = (255, 0, 0)
        text_play = fonte.render('Play', True, cor_text)
        text_Confi = fonte1.render('Configuração', True, cor_text)
        text_sair = fonte.render('Sair', True, cor_text)
        text_nome = fonte2.render('Caça mina simuleitor', True, cor_text)
        text_cred = fonte3.render('By Raul C. Caça mina simuleitor V3', True, cor_text)

        tempo = pygame.time.Clock()
        while True:
            self.Tela.Def_Mxy()

            tempo.tick(60)
            self.Tela.Tela.blit(fundo, (0, 0))

            # Botoes e suas dinamicas
            cor = []
            for c in range(0, 3):
                cor.append((255, 160, 122))

            for v in muda:
                cor.insert(v, cor_toque)

            muda = []

            Bplay = pygame.draw.rect(self.Tela.Tela, cor[0], (lag * 0.40, alt * 0.35, lag * 0.20, alt * 0.10), 0, 50)
            if Bplay.collidepoint(mxy[0], mxy[1]):
                muda.append(0)

            self.Tela.Tela.blit(text_play, (lag * 0.47, alt * 0.37))

            Bconfi = pygame.draw.rect(self.Tela.Tela, cor[1], (lag * 0.40, alt * 0.47, lag * 0.20, alt * 0.10), 0, 50)
            if Bconfi.collidepoint(mxy[0], mxy[1]):
                muda.append(1)

            self.Tela.Tela.blit(text_Confi, (lag * 0.430, alt * 0.49))

            Bsair = pygame.draw.rect(self.Tela.Tela, cor[2], (lag * 0.40, alt * 0.59, lag * 0.20, alt * 0.10), 0, 50)
            if Bsair.collidepoint(mxy[0], mxy[1]):
                muda.append(2)

            self.Tela.Tela.blit(text_sair, (lag * 0.47, alt * 0.61))

            # eventos
            for acao in pygame.event.get():
                self.Tela.fechar(acao)

                if self.Tela.mosuse(acao, 1, 0, True):

                    if Bsair.collidepoint(mxy[0], mxy[1]):
                        self.Tela.fechar(True)

                    if Bconfi.collidepoint(mxy[0], mxy[1]):
                        Menu = MenuConfiguracao(self.Nome, self.NUM_Res, self.Dados)
                        Menu.Print_Menu_Configuracao()
                        self.Tela.fechar(True)

                    if Bplay.collidepoint(mxy[0], mxy[1]):
                        self.Tela.fechar(True)

            # Texto
            self.Tela.Tela.blit(text_nome, (lag * 0.22, alt * 0.11))

            self.Tela.Tela.blit(text_cred, (lag * 0.77, alt * 0.94))
            pygame.display.update()

    def AbriMenu(self):
        Menu = MenuConfiguracao(self.Nome, self.NUM_Res, self.Dados)
        Menu.Print_Menu_Configuracao()

