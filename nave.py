import pygame
import sys
from pygame.locals import *

largura = 500
altura = 400

class Bala(pygame.sprite.Sprite):
    def __init__(self, posy, posx):
        pygame.sprite.Sprite.__init__(self)
        self.dispara = pygame.image.load("imagens/municao.png")

        self.rect = self.dispara.get_rect()
        self.velocidadeDisparo = 1
        self.rect.top = posy
        self.rect.left = posx

    def trajeto(self):
        self.rect.top = self.rect.top - self.velocidadeDisparo

    def colocar(self, superficieBala):
        superficieBala.blit(self.dispara, self.rect)

class NavePrincipal(pygame.sprite.Sprite):
    def __init__(self):
        #Nave Principal
        pygame.sprite.Sprite.__init__(self)
        self.nave_principal = pygame.image.load("imagens/NavePrincipal.png")

        #Posicao da nave na tela
        self.rect = self.nave_principal.get_rect()
        self.rect.centerx = altura/2
        self.rect.centery = largura-50

        #Disparo, vida e velocidade
        self.listaDisparo = []
        self.vida = True
        self.velocidade = (1)

    def movimento(self):
        if self.vida == True:
            if self.rect.left <= -30:
                self.rect.left = 30

            if self.rect.right > 530:
                self.rect.right = 530

            if self.rect.top <= -15:
                self.rect.top = -15

            if self.rect.bottom > 415:
                self.rect.bottom = 415

    def disparar(self, x, y):
        municaoBala = Bala(x, y)
        self.listaDisparo.append(municaoBala)

    def colocar(self, superficie):
        superficie.blit(self.nave_principal, self.rect)

def SpaceInvaders():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Invasão Alienígena")

    jogador = NavePrincipal()
    fundo = pygame.image.load("imagens/Mapa.JPG")
    jogando = True

    balaProjetil = Bala(largura / 2, altura - 200)

    while True:
        jogador.movimento()
        balaProjetil.trajeto()
        keys = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        if keys [K_LEFT]:
            jogador.rect.left -= jogador.velocidade
        if keys [K_RIGHT]:
            jogador.rect.right += jogador.velocidade
        if keys [K_UP]:
            jogador.rect.top -= jogador.velocidade
        if keys [K_DOWN]:
            jogador.rect.bottom += jogador.velocidade
        if keys == [K_0]:
            x, y = jogador.rect.center
            jogador.disparar(x, y)

        tela.blit(fundo, (0,0))
        balaProjetil.colocar(tela)
        jogador.colocar(tela)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajeto()
                if x.rect.top < 100:
                    jogador.listaDisparo.remove(x)
        pygame.display.update()

SpaceInvaders()
