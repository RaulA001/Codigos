#metodos paras as clases janelas
import pygame
import sys


def deCodRes(telaTamanho):
    if telaTamanho == 0:
        pygame.init()
        d = pygame.display.Info()
        lag, alt = d.current_w, d.current_h
    elif telaTamanho == 1:
        lag = 960
        alt = 540
    elif telaTamanho == 2:
        lag = 640
        alt = 360
    return [lag, alt]

def dfMxy():
    mx, my = pygame.mouse.get_pos()
    Mxy = (mx, my)
    return Mxy

deCodRes(0)