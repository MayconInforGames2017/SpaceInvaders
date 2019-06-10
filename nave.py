import pygame
import sys
import random
from pygame.locals import *

largura = 500
altura = 400

class NaveInimiga(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        #DISPAROS
        pygame.sprite.Sprite.__init__(self)
        self.nave_inimiga = pygame.image.load('imagens/NaveInimiga.PNG')

        self.rect = self.nave_inimiga.get_rect()

        self.listaInimigos = []
        self.velocidade_inimigo = 1
        self.rect.top = posy
        self.rect.left = posx

    def colocar(self, superficie):
        superficie.blit(self.nave_inimiga, self.rect)


class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        #DISPAROS
        pygame.sprite.Sprite.__init__(self)
        self.bala_principal = pygame.image.load('imagens/Municao(naveprincipal).JPG')

        self.rect = self.bala_principal.get_rect()
        self.velocidade_bala = 2
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
        self.velocidade = 2

    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 3:
                self.rect.left = 3

            if self.rect.right > 497:
                self.rect.right = 497

            if self.rect.top <= 3:
                self.rect.top = 3

            if self.rect.bottom > 397:
                self.rect.bottom = 397



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

    #VIDA INIMIGO
    vida_inimigo = True

    #POSIÇÃO INIMIGO
    posX = random.random()*500
    posY = random.random()*50

    #INIMIGO
    inimigo = NaveInimiga(posX,posY)

    bala_principal = Bala(largura / 2, altura - 60)

    while True :
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

        if vida_inimigo == True:
            inimigo.rect.top += inimigo.velocidade_inimigo

        #OBJETOS
        tela.blit(fundo, (0,0))
        jogador.colocar(tela)
        inimigo.colocar(tela)

        if len (inimigo.listaInimigos) > 0:
            for x in inimigo.listaInimigos:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < 400:
                    inimigo.listaInimigos.remove(x)

        if len (jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < 0:
                    jogador.listaDisparo.remove(x)
        pygame.display.update()

InvasaoAlienigina()
