# -*- coding: cp1252 -*-
import pygame
from pygame import *
from sys import exit
from tlk import *



###########################################FUNCOES########################
#encapsular depois



def start():
    global a, b, c, tab
    a = Tabuleiro()
    tab = a.cria_tabuleiro()

    b = Jogador("j1", 1)
    c = Jogador("j2", 2)

    b.set_pecas() 
    c.set_pecas()

    posiciona_pecas()

    
def get_jogador(jogador):
    if b.jogador == jogador:
        return b
    return c

def de_quem_eh_a_vez():
    if b.vez:
        return b
    return c

def botao(x, y, lado_esq, lado_dir, lado_superior, lado_inferior):
    return (lado_dir >= x >= lado_esq) and (lado_inferior >= y >= lado_superior)

def check_pecas(tipo, jogador, tabuleiro):
    posicoes = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tab[i][j] != 0:
                if tabuleiro[i][j].jogador == jogador:
                    if tabuleiro[i][j].tipo == tipo:
                        posicoes.append((i,j))
    
    return posicoes


def posiciona_pecas():
    linha_superior = ["cat1", "h_i1", "a1", "cav1", "gen0", "cas0", "cav2", "a2", "h_i2", "cat2"] 
    linha_inferior = ["h_cav1", "a3", "i1", "i2", "e1", "e2", "i3", "i4", "a4", "h_cav2"]
    for j in range(len(linha_superior)):
        c.posiciona_peca(linha_superior[j], (0, j), tab)
        c.posiciona_peca(linha_inferior[j], (1, j), tab)
        b.posiciona_peca(linha_superior[j], (9, j), tab)
        b.posiciona_peca(linha_inferior[j], (8, j), tab)
    return True


def check_posicoes():
    posicoes = {}
    posicoes[casp] = check_pecas("castelo", 1, tab)
    posicoes[genp] = check_pecas("general", 1, tab)
    posicoes[arqp] = check_pecas("arqueiro", 1, tab)
    posicoes[catp] = check_pecas("catapulta", 1, tab)
    posicoes[cavp] = check_pecas("cavalaria", 1, tab)
    posicoes[escp] = check_pecas("escudeiro", 1, tab)
    posicoes[hcavp] = check_pecas("h_cavalaria", 1, tab)
    posicoes[hip] = check_pecas("h_infantaria", 1, tab)
    posicoes[ip] = check_pecas("infantaria", 1, tab)

    posicoes[casb] = check_pecas("castelo", 2, tab)
    posicoes[genb] = check_pecas("general", 2, tab)
    posicoes[arqb] = check_pecas("arqueiro", 2, tab)
    posicoes[catb] = check_pecas("catapulta", 2, tab)
    posicoes[cavb] = check_pecas("cavalaria", 2, tab)
    posicoes[escb] = check_pecas("escudeiro", 2, tab)
    posicoes[hcavb] = check_pecas("h_cavalaria", 2, tab)
    posicoes[hib] = check_pecas("h_infantaria", 2, tab)
    posicoes[ib] = check_pecas("infantaria", 2, tab)
    return posicoes

###########################################INICIALIZACOES############
start()

################################################
wait = []
jogador = []
diferente = False




pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("The Last King")


background = pygame.image.load("main_screen.png").convert()
tabuleiro = pygame.image.load("tabuleiro.png").convert()

selecionar = pygame.image.load("selecionar.png").convert()
selecionar.set_colorkey((255, 0, 0))

### TIME AZUL ###
casb = pygame.image.load("casb.png").convert()
genb = pygame.image.load("genb.png").convert()
arqb = pygame.image.load("arqb.png").convert()
catb = pygame.image.load("catb.png").convert()
cavb = pygame.image.load("cavb.png").convert()
escb = pygame.image.load("escb.png").convert()
hcavb = pygame.image.load("hcavb.png").convert()
hib = pygame.image.load("hib.png").convert()
ib = pygame.image.load("ib.png").convert()

casb.set_colorkey((40, 200, 255))
genb.set_colorkey((40, 200, 255))
arqb.set_colorkey((40, 200, 255))
catb.set_colorkey((40, 200, 255))
cavb.set_colorkey((40, 200, 255))
escb.set_colorkey((40, 200, 255))
hcavb.set_colorkey((40, 200, 255))
hib.set_colorkey((40, 200, 255))
ib.set_colorkey((40, 200, 255))






### TIME  BRANCO ###

casp = pygame.image.load("casp.png").convert()
genp = pygame.image.load("genp.png").convert()
arqp = pygame.image.load("arqp.png").convert()
catp= pygame.image.load("catp.png").convert()
cavp = pygame.image.load("cavp.png").convert()
escp = pygame.image.load("escp.png").convert()
hcavp = pygame.image.load("hcavp.png").convert()
hip = pygame.image.load("hip.png").convert()
ip = pygame.image.load("ip.png").convert()

casp.set_colorkey((255, 255, 255))
genp.set_colorkey((255, 255, 255))
arqp.set_colorkey((255, 255, 255))
catp.set_colorkey((255, 255, 255))
cavp.set_colorkey((255, 255, 255))
escp.set_colorkey((255, 255, 255))
hcavp.set_colorkey((255, 255, 255))
hip.set_colorkey((255, 255, 255))
ip.set_colorkey((255, 255, 255))


####explosao#############################################


explode1 = pygame.image.load("explode1.png").convert()
explode2 = pygame.image.load("explode2.png").convert()

explode21 = pygame.image.load("explode21.png").convert()
explode22 = pygame.image.load("explode22.png").convert()
explode23 = pygame.image.load("explode23.png").convert()


explode1.set_colorkey((240, 240, 240))
explode2.set_colorkey((240, 240, 240))

explode21.set_colorkey((0, 0, 0))
explode22.set_colorkey((0, 0, 0))
explode23.set_colorkey((0, 0, 0))



def explosao(i,j):
    sequencia = [explode1, explode2]
    for img in sequencia:
                
                pygame.time.delay(100)
                screen.blit(img, (j * 60, i * 60))
                pygame.display.update()
                pygame.time.delay(100)


def explosao2(i,j):
    sequencia = [explode21, explode22, explode23]
    for img in sequencia:
                
                pygame.time.delay(80)
                screen.blit(img, (j * 60, i * 60))
                pygame.display.update()
                pygame.time.delay(80)
###########################################################

font = pygame.font.SysFont("arial", 16)
font2 = pygame.font.SysFont("arial", 58);
clock = pygame.time.Clock()



posicoes = check_posicoes()



while True:
    
    for event in pygame.event.get():
        screen.blit(background, (0,0))
        if event.type == QUIT:
            exit()

        x, y = pygame.mouse.get_pos()
        if botao(x, y, 300, 430, 345, 420):
            if event.type == MOUSEBUTTONDOWN:
                               
                start()
                b.vez = True
                while True:
                    clock.tick(35)
                    if b.castelo.hp < 1:
                        screen.blit(font2.render(" Jogador " + str(c.jogador) + " é o vencedor.", True, (255, 0, 0)), (0, 230))
                        pygame.display.update()
                        pygame.time.delay(4000)
                        break
                    if c.castelo.hp < 1:
                        screen.blit(font2.render(" Jogador " + str(b.jogador) + " é o vencedor.", True, (255, 0, 0)), (0, 230))
                        pygame.display.update()
                        pygame.time.delay(4000)
                        break
                        
                        
                    x, y = pygame.mouse.get_pos()
                    i, j = int(y/60.), int(x/60.)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()

                    screen.blit(tabuleiro, (0,0))
                    if diferente:
                        posicoes = check_posicoes()
                    
                    for imagem in posicoes:
                        for posicao in posicoes[imagem]:
                            f,g = posicao
                            screen.blit(imagem, (g * 60, f * 60))

                  
                    
                    
                    if botao(x, y, 626, 780, 530, 563):
                        clock.tick(14)
                        if event.type == MOUSEBUTTONDOWN:
                            if b.vez:
                                b.end_turn(c)
                                wait = []
                                
                            else:
                                c.end_turn(b)
                                wait = []

                        

                    
                    
        
                   
                    

                    #informaçoes dos jogadores
                    screen.blit(font.render(" Jogador : " + str(c.jogador), True, (0, 0, 255)), (620, 0))
                    screen.blit(font.render(" Pontos de ataque : " + str(c.pontos_atq), True, (0, 0, 255)), (620, 20))
                    screen.blit(font.render(" Pontos de movimento : "  + str(c.pontos_move), True, (0, 0, 255)), (620, 40))

                    screen.blit(font.render(" Jogador : " + str(b.jogador), True, (0, 0, 255)), (620, 400))
                    screen.blit(font.render(" Pontos de ataque : " + str(b.pontos_atq), True, (0, 0, 255)), (620, 420))
                    screen.blit(font.render(" Pontos de movimento : " + str(b.pontos_move), True, (0, 0, 255)), (620, 440))

                    diferente = False
                    if (i <= 9 and j <= 9) and tab[i][j] != 0:
                        screen.blit(font.render(" Tipo: " + str(tab[i][j].tipo), True, (0, 0, 255)), (620, 200))
                        screen.blit(font.render(" HP: " + str(tab[i][j].hp), True, (0, 0, 255)), (620, 220))
                        screen.blit(font.render(" Ataque: " + str(tab[i][j].atq), True, (0, 0, 255)), (620, 240))
                        screen.blit(font.render(" Movimentos consumidos: " + str(tab[i][j].movimento), True, (0, 0, 255)), (620, 260))
                        screen.blit(font.render(" Ataques consumidos: " + str(tab[i][j].pontos_min_atq), True, (0, 0, 255)), (620, 280))
                        screen.blit(font.render(" Alcance de ataque: " + str(tab[i][j].alcance_max_atq), True, (0, 0, 255)), (620, 300))
                        if event.type == MOUSEBUTTONDOWN:
                            if len(wait) == 1 or tab[i][j].jogador == de_quem_eh_a_vez().jogador:
                    
                                if (i,j) in wait:
                                    wait = []
                                    
                                if wait == [] and tab[i][j] == 0:
                                    wait = []
                                    
                                if len(wait) == 1 and wait[0] == (i,j):
                                    wait = []
                                        
                                if wait == [] and tab[i][j] != 0:
                                    wait.append((i,j))
                                    jogador.append(get_jogador(tab[i][j].jogador))
                                         
                                        

                                if len(wait) == 1 and wait[0] != (i,j):
                                    wait.append((i,j))
                                    #jogador[0].move(wait[0],wait[1], tab)
                                    ab, cd = wait[1]
                                    ba, dc = wait[0]
                                    #if tab[ab][cd] != 0 and tab[ba][dc].pontos_min_atq <= de_quem_eh_a_vez().pontos_atq:
                                       # explosao2(ab,cd)
                                       # pygame.time.delay(100)

                                    #if tab[ba][dc].pontos_min_atq > de_quem_eh_a_vez().pontos_atq:
                                     #   explosao(ba,dc)
                                      #  pygame.time.delay(100)
                                        
                                    if jogador[0].move(wait[0],wait[1], tab) == 'atacou':
                                        explosao2(ab,cd)
                                        pygame.time.delay(100)
                                    else:
                                        explosao(ba,dc)
                                        pygame.time.delay(100)

                                    #if tab[ba][dc] != 0:
                                     #   explosao(ba, dc)
                                      #  pygame.time.delay(100)
                                        
                                    wait = []
                                    diferente = True
                                    jogador = []
                                
                                   
                                
                                

                    if (i <= 9 and j <= 9) and tab[i][j] == 0 and event.type == MOUSEBUTTONDOWN:
                        if (i,j) in wait:
                            wait = []
                            
                        if wait == [] and tab[i][j] == 0:
                            wait = []
                            
                        if len(wait) == 1 and wait[0] == (i,j):
                            wait = []
                                
                        if wait == [] and tab[i][j] != 0:
                            wait.append((i,j))
                            jogador.append(get_jogador(tab[i][j].jogador))
                                 
                                

                        if len(wait) == 1 and wait[0] != (i,j):
                            wait.append((i,j))
                            jogador[0].move(wait[0],wait[1], tab)
                            ab, cd = wait[0]
                            if tab[ab][cd] != 0:
                                explosao(ab,cd)
                                pygame.time.delay(100)
                                
                            wait = []
                            diferente = True
                            jogador = []
                                
                                
                            
                    
                    if len(wait) == 1:
                        w, z = wait[0]
                        screen.blit(selecionar, (z * 60, w * 60))

                    print wait 
                    pygame.display.update()
                
        

    pygame.display.update()        
