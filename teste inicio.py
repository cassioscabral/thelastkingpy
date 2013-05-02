import pygame
from pygame import *
from sys import exit
from tlk import *

a = Tabuleiro()
tab = a.cria_tabuleiro()

b = Jogador("cassio", 1)
c = Jogador("henrique", 2)

b.set_pecas() 
c.set_pecas()


def posiciona_pecas():
    linha_superior = ["cat1", "h_i1", "a1", "cav1", "gen0", "cas0", "cav2", "a2", "h_i2", "cat2"] 
    linha_inferior = ["h_cav1", "a3", "i1", "i2", "e1", "e2", "i3", "i4", "a4", "h_cav2"]
    for j in range(len(linha_superior) - 1):
        c.posiciona_peca(linha_superior[j], (0,j), tab)
        c.posiciona_peca(linha_inferior[j], (1,j), tab)
        b.posiciona_peca(linha_superior[j], (9, j), tab)
        b.posiciona_peca(linha_inferior[j], (8, j), tab)
    return True
    


def check_pecas(tipo, jogador, tabuleiro):
    i = -1
    j = -1
    posicoes = []
    for linha in tabuleiro:
        i += 1
        for coluna in linha:
            j += 1
            if (i < 10 and j < 10) and tab[i][j] != 0:
                if tabuleiro[i][j].jogador == jogador:
                    if tabuleiro[i][j].tipo == tipo:
                        posicoes.append((i,j))
        j = 0
    return posicoes

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
