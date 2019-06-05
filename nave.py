import pygame
import sys
from pygame.locals import *

largura = 500
altura = 400

class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        #DISPAROS
        pygame.sprite.Sprite.__init__(self)
        self.bala_principal = pygame.image.load('imagens/Tiro(naveprincipal).JPG')

        self.rect = self.bala_principal.get_rect()
        self.velocidade_bala = 3
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidade_bala

    def colocar(self, superficie):
        superficie.blit(self.bala_principal, self.rect)


class NavePrincipal(pygame.sprite.Sprite):
    def __init__(self):
        #NAVE PRINCIPAL
        pygame.sprite.Sprite.__init__(self)
        self.nave_principal = pygame.image.load('imagens/NavePrincipal.PNG')

        #POSIÇÃO DA NAVE NA TELA
        self.rect = self.nave_principal.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura-50

        #DISPARO, VIDA E VELOCIDADE
        self.listaDisparo = []
        self.vida = True
        self.velocidade = (3)

    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0

            if self.rect.right > 500:
                self.rect.right = 500

            if self.rect.top <= 0:
                self.rect.top = 0

            if self.rect.bottom > 400:
                self.rect.bottom = 400



    def disparar(self, x, y):
        minha_bala = Bala(x,y)
        self.listaDisparo.append(minha_bala)

    def colocar(self, superficie):
        superficie.blit(self.nave_principal, self.rect)



def InvasaoAlienigina():
    pygame.init()
    #DIMENSÕES DA TELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Invasão Alienígena')

    #JOGADOR E FUNDO
    jogador = NavePrincipal()
    fundo = pygame.image.load('imagens/Mapa.JPG')
    #JOGANDO
    jogando = True

    bala_principal = Bala(largura / 2, altura - 60)
    #FRAMES POR SEGUNDO
    fps = pygame.time.Clock()

    while True :
        fps.tick(70)
        jogador.movimento()
        bala_principal.trajetoria()
        keys = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x-1,y-22)

        if keys [K_LEFT]:
            jogador.rect.left -= jogador.velocidade
        if keys [K_RIGHT]:
            jogador.rect.right += jogador.velocidade
        if keys [K_UP]:
            jogador.rect.top -= jogador.velocidade
        if keys [K_DOWN]:
            jogador.rect.bottom += jogador.velocidade



        #OBJETOS
        tela.blit(fundo, (0,0))
        jogador.colocar(tela)
        if len (jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < 0:
                    jogador.listaDisparo.remove(x)
        pygame.display.update()

InvasaoAlienigina()
