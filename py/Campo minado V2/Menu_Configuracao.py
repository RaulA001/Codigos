from janela import *


class MenuConfiguracao(Janela):
    def __init__(self, nome, tamnho, dt=[6, 8, 8]):
        super().__init__(nome, tamnho, dt)

    def Print_Menu_Configuracao(self):
        mudaTela=False
        valido = False
        pygame.init()
        while True:
            if mudaTela:
                pygame.display.quit()
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
            fonte2 = pygame.font.SysFont("arial", int((alt * 0.13) * 0.75), True, True)
            fonte3 = pygame.font.SysFont("arial", int((alt * 0.03) * 0.75), True, False)
            fonte4 = pygame.font.SysFont("arial", int((lag * 0.04) * 0.9), True, True)

            # Textos
            cor_text = (255, 0, 0)
            text_Resolucao = fonte.render('Resolução', True, cor_text)
            text_Detale = fonte.render('Detalhes', True, cor_text)
            text_Volta = fonte.render('Volta', True, cor_text)
            text_TM = fonte.render('Tamnho do tabuleiro', True, cor_text)
            text_rec1 = fonte.render('1920 x 1080', False, cor_text)
            text_rec2 = fonte.render('960 x 540', False, cor_text)
            text_rec3 = fonte.render('640 x 360', False, cor_text)
            text_nome = fonte2.render('Caça mina simuleitor', True, cor_text)
            text_cred = fonte3.render('By Raul C. Caça mina simuleitor V3', True, cor_text)

            # detales
            if len(self.Dados) == 0:
                dad = [6, 8, 8]
                self.Dados = dad
            else:
                dad = self.Dados
            dad1t = f'Numero de bombas | {dad[0]}'
            dad2t = f'X = {dad[1]}'
            dad3t = f'Y = {dad[2]}'
            text_input = [0, dad1t, dad2t, dad3t]

            conf = False
            detales = False

            ok = False
            on = True
            mudaTela = False
            mostra_erro = False
            edit = 0

            tempo = pygame.time.Clock()
            while on:
                self.Tela.Def_Mxy()

                tempo.tick(60)
                self.Tela.Tela.blit(fundo, (0, 0))

                # Botoes e suas dinamicas
                cor = []
                for c in range(0, 6):
                    cor.append((255, 160, 122))

                rect = pygame.draw.rect(self.Tela.Tela, (135,206,235), (0, 0, lag * 0.27, alt * 120))

                for v in muda:
                    cor.insert(v, cor_toque)

                muda = []

                Bresolucao = pygame.draw.rect(self.Tela.Tela, cor[0], (lag * 0.03, alt * 0.03, lag * 0.20, alt * 0.10), 0, 50)
                if Bresolucao.collidepoint(mxy[0], mxy[1]):
                    muda.append(0)

                self.Tela.Tela.blit(text_Resolucao, (lag * 0.055, alt * 0.05))

                Bdetale = pygame.draw.rect(self.Tela.Tela, cor[1], (lag * 0.03, alt * 0.18, lag * 0.20, alt * 0.10), 0, 50)
                if Bdetale.collidepoint(mxy[0], mxy[1]):
                    muda.append(1)

                self.Tela.Tela.blit(text_Detale, (lag * 0.070, alt * 0.2))

                Bvolta = pygame.draw.rect(self.Tela.Tela, cor[2], (lag * 0.03, alt * 0.85, lag * 0.20, alt * 0.10), 0, 50)
                if Bvolta.collidepoint(mxy[0], mxy[1]):
                    muda.append(2)

                self.Tela.Tela.blit(text_Volta, (lag * 0.09, alt * 0.87))

                # eventos
                for acao in pygame.event.get():
                    self.Tela.fechar(acao)

                    if acao.type == pygame.KEYDOWN:
                        if edit != 0:
                            if acao.key == pygame.K_BACKSPACE:

                                apaga = False
                                if edit == 1 and len(text_input[1]) >= 20:
                                    apaga = True
                                elif edit == 2 and len(text_input[2]) >= 5:
                                    apaga = True
                                elif edit == 3 and len(text_input[3]) >= 5:
                                    apaga = True
                                if apaga:
                                    text_input[edit] = text_input[edit][:-1]

                            else:
                                if acao.unicode.isnumeric():
                                    text_input[edit] += acao.unicode

                    Nbombas = (text_input[1][19:])
                    x = (text_input[2][3:])
                    y = (text_input[3][3:])
                    try:
                        Nbombas = int(Nbombas)
                        x = int(x)
                        y = int(y)
                    except:
                        valido = False
                    else:
                        if x*y > Nbombas:
                            valido = True
                            self.SalvarDados(Nbombas, x, y)
                        else:
                            valido = False

                    if self.Tela.mosuse(acao, 1, 0, True):

                        if Bvolta.collidepoint(mxy[0], mxy[1]):

                            if valido:
                                self.AbriMenu()
                                self.Tela.fechar(True)
                            else:

                                txErro2 = f'Erro; tem {Nbombas} bombas e uma área de {x*y}'
                                text_erro2 = fonte4.render(txErro2, True, (255, 0, 0))
                                mostra_erro = True

                        if Bdetale.collidepoint(mxy[0], mxy[1]):
                            if conf:
                                conf = not conf
                            detales = not detales

                        if conf or detales and ok:
                            if Bres1.collidepoint(mxy[0], mxy[1]):
                                if conf:
                                    self.NUM_Res = 0
                                    mudaTela=True
                                    on = False
                                elif detales:
                                    edit = 1

                            elif Bres2.collidepoint(mxy[0], mxy[1]):
                                if conf:
                                    self.NUM_Res = 1
                                    on = False
                                elif detales:
                                    edit = 2

                            elif Bres3.collidepoint(mxy[0], mxy[1]):
                                if conf:
                                    self.NUM_Res = 2
                                    on = False
                                elif detales:
                                    edit = 3

                    if self.Tela.mosuse(acao, 1, Bresolucao, False):
                        if detales:
                            detales = not detales
                        conf = not conf

                if conf:
                    ok = True
                    Bres1 = pygame.draw.rect(self.Tela.Tela, cor[3], (lag * 0.31, alt * 0.03, lag, alt * 0.10), 0, 50)

                    if Bres1.collidepoint(mxy[0], mxy[1]):
                        muda.append(3)
                    self.Tela.Tela.blit(text_rec1, (lag * 0.60, alt * 0.05))

                    Bres2 = pygame.draw.rect(self.Tela.Tela, cor[4], (lag * 0.31, alt * 0.18, lag, alt * 0.10), 0, 50)

                    if Bres2.collidepoint(mxy[0], mxy[1]):
                        muda.append(4)
                    self.Tela.Tela.blit(text_rec2, (lag * 0.6, alt * 0.20))

                    Bres3 = pygame.draw.rect(self.Tela.Tela, cor[5], (lag * 0.31, alt * 0.33, lag, alt * 0.10), 0, 50)

                    if Bres3.collidepoint(mxy[0], mxy[1]):
                        muda.append(5)
                    self.Tela.Tela.blit(text_rec3, (lag * 0.6, alt * 0.35))

                if detales:
                    ok=True
                    Bres1 = pygame.draw.rect(self.Tela.Tela, cor[3], (lag * 0.31, alt * 0.03, lag, alt * 0.10), 0, 50)

                    if Bres1.collidepoint(mxy[0], mxy[1]):
                        muda.append(3)

                    Bres2 = pygame.draw.rect(self.Tela.Tela, cor[4], (lag * 0.4, alt * 0.33, lag * 0.15, alt * 0.1), 0, 50)

                    if Bres2.collidepoint(mxy[0], mxy[1]):
                        muda.append(4)

                    Bres3 = pygame.draw.rect(self.Tela.Tela, cor[5], (lag * 0.8, alt * 0.33, lag * 0.15, alt * 0.10), 0, 50)

                    if Bres3.collidepoint(mxy[0], mxy[1]):
                        muda.append(5)

                    Binfo = pygame.draw.rect(self.Tela.Tela, (255, 160, 122), (lag * 0.31, alt * 0.18, lag, alt * 0.10), 0, 50)

                    self.Tela.Tela.blit(text_TM, (lag * 0.535, alt * 0.20))

                    text_S1 = fonte.render(text_input[1], True, cor_text)
                    self.Tela.Tela.blit(text_S1, (lag * 0.535, alt * 0.05))

                    text_S2 = fonte.render(text_input[2], True, cor_text)
                    self.Tela.Tela.blit(text_S2, (lag * 0.435, alt * 0.35))

                    text_S3 = fonte.render(text_input[3], True, cor_text)
                    self.Tela.Tela.blit(text_S3, (lag * 0.835, alt * 0.35))
                if mostra_erro:
                    self.Tela.Tela.blit(text_erro2, (lag * 0.30, alt * 0.70))

                pygame.display.update()

    def AbriMenu(self):
        from Main_menu import MainMenu
        cu = MainMenu(self.Nome, self.NUM_Res, self.Dados)
        cu.Print_Main_menu()

    def SalvarDados(self, NB, X, Y):
        self.Dados = [NB, X, Y]


