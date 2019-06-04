import pygame, sys
from pygame.locals import *

largura = 500
altura = 400

class Municao(pygame.sprite.Sprite):
    def __init__(self, posy, posx):
        #Disparos
        pygame.sprite.Sprite.__init__(self)
        self.disparaMunicao = pygame.image.load("imagens/Tiro(naveprincipal).JPG")

        self.rect = self.disparaMunicao.get_rect()
        self.velocidadeDisparo = 3
        self.rect.top = posy
        self.rect.left = posx

    def trajeto(self):
        self.rect.top = self.rect.top - self.velocidadeDisparo

    def colocar(self, superficie):
        superficie.blit(self.disparaMunicao, self.rect)

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
        municaoBala = Municao(x, y)
        self.listaDisparo.append(municaoBala)

    def colocar(self, superficie):
        superficie.blit(self.nave_principal, self.rect)

def SpaceInvaders():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Invasão Alienígena")
    #Jogador e fundo da tela
    jogador = NavePrincipal()
    fundo = pygame.image.load("imagens/Mapa.JPG")
    #Jogando
    jogando = True

    municaoProjetil = Municao(largura / 2, altura - 60)
    #Frames por segundo
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(70)
        jogador.movimento()
        municaoProjetil.trajeto()
        keys = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_SPACE:
                    x, y = jogador.rect.center
                    jogador.disparar(x-1,y-22)
        if keys [K_LEFT]:
            jogador.rect.left -= jogador.velocidade
        if keys [K_RIGHT]:
            jogador.rect.right += jogador.velocidade
        if keys [K_UP]:
            jogador.rect.top -= jogador.velocidade
        if keys [K_DOWN]:
            jogador.rect.bottom += jogador.velocidade

        tela.blit(fundo, (0,0))
        #municaoProjetil.colocar(tela)
        jogador.colocar(tela)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajeto()
                if x.rect.top < 100:
                    jogador.listaDisparo.remove(x)

        pygame.display.update()

SpaceInvaders()
