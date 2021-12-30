import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#som def
booom = pygame.mixer.Sound('Boom.wav')
booom.set_volume(0.40)

#tela tamanho
telaTamanho = 1

if telaTamanho == 0:
    lag = 1920
    alt = 1080
elif telaTamanho == 1:
    lag = 960
    alt = 540
elif telaTamanho == 2:
    lag = 640
    alt = 360
else:
    lag = 960
    alt = 540

#tela on
tela = pygame.display.set_mode((lag, alt))
pygame.display.set_caption('💓Caça mina simuleitor💓')

#fundo
Pfundo = pygame.image.load('fundo.gif')
Pfundo = pygame.transform.scale(Pfundo, (lag, alt))

#dados
x = lag/2
y = alt/2
vel = lag*0.005
vely = alt*0.005

#Tempo/Fonte
tempo = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", int((alt*0.07)*0.75), True, False)
fonte1 = pygame.font.SysFont("arial", int((alt*0.055)*0.75), True, False)
fonte2 =  pygame.font.SysFont("arial", int((alt*0.13)*0.75), True, True)
fonte3 =  pygame.font.SysFont("arial", int((alt*0.03)*0.75), True, False)
fonte4 =  pygame.font.SysFont("arial", int((alt*0.03)*0.75), True, False)

cor_botao = (255,160,122)
cor_botao1 = cor_botao2 = cor_botao3 = cor_botao

#go
while True:
    #Tempo emp, tela cor emp
    tempo.tick(120)
    tela.fill((152,251,152))
    #tela.blit(Pfundo, (0, 0))


    #textos
    cor_text = (255, 0, 0)
    text_play = fonte.render('Play', True, cor_text)
    text_Confi = fonte1.render('Configuração', True, cor_text)
    text_sair = fonte.render('Sair', True, (cor_text))
    text_nome = fonte2.render('Caça mina simuleitor', True, (cor_text))
    text_cred = fonte3.render('By Raul C. Caça mina simuleitor V3', True, (cor_text))

    Bplay = pygame.draw.rect(tela, cor_botao1, (lag * 0.40, alt * 0.35, lag * 0.20, alt * 0.10), 0, 50)

    Bconfi = pygame.draw.rect(tela, cor_botao2, (lag * 0.40, alt * 0.47, lag * 0.20, alt * 0.10), 0, 50)

    Bsair = pygame.draw.rect(tela, cor_botao3, (lag * 0.40, alt * 0.59, lag * 0.20, alt * 0.10), 0, 50)

    #GET MOUSE
    mx, my = pygame.mouse.get_pos()

    #get teclas
    for acao in pygame.event.get():
        #sair
        if acao.type == QUIT:
            print(lag, alt)
            pygame.quit()
            exit()
        '''if acao.type == KEYDOWN:
            if acao.key == K_a:
                x -= vel

            if acao.key == K_d:
                x += vel

            if acao.key == K_s:
                y += vely

            if acao.key == K_w:
                y -= vely'''
        #teclado
        if pygame.key.get_pressed()[K_a]:
            x -= vel
        if pygame.key.get_pressed()[K_d]:
            x += vel

        if pygame.key.get_pressed()[K_w]:
            y -= vely
        if pygame.key.get_pressed()[K_s]:
            y += vely

        #mouse
        if acao.type == MOUSEBUTTONDOWN:
            print('')
            print(mx, my, end=(""))

            if acao.button == 1:
                print(' Esquerdo')
                #botoes apertados
                #if Bsair.collidepoint(mx, my):
                #    pygame.quit()
                #    quit()
#
                #if Bconfi.collidepoint(mx, my):
                #    pygame.quit()
                #    quit()
#
                #if Bplay.collidepoint(mx, my):
                #    pygame.quit()
                #    quit()

            if acao.button == 3:
                print(' Direita')

    #desenhos
    cor_botao1 = cor_botao2 = cor_botao3 = cor_botao
    cor_botao_toque = (240,128,128)


    if Bplay.collidepoint(mx, my):
        cor_botao1 = cor_botao_toque

    Bplay = pygame.draw.rect(tela, cor_botao1, (lag * 0.40, alt * 0.35, lag * 0.20, alt * 0.10), 0, 50)
    tela.blit(text_play, (lag * 0.47, alt * 0.37))

    if Bconfi.collidepoint(mx, my):
        cor_botao2 = cor_botao_toque
    Bconfi = pygame.draw.rect(tela, cor_botao2, (lag*0.40, alt*0.47, lag*0.20, alt*0.10), 0, 50)
    tela.blit(text_Confi, (lag*0.430, alt*0.49))

    if Bsair.collidepoint(mx, my):
        cor_botao3 = cor_botao_toque

    Bsair = pygame.draw.rect(tela, cor_botao3, (lag*0.40, alt*0.59, lag*0.20, alt*0.10), 0, 50)
    tela.blit(text_sair, (lag * 0.47, alt * 0.61))


    tela.blit(text_nome, (lag * 0.22, alt * 0.11))
    if telaTamanho != 0:
        tela.blit(text_cred, (lag * 0.77, alt * 0.94))
    else:
        tela.blit(text_cred, (lag * 0.67, alt * 0.84))

    pygame.display.update()
