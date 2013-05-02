# -*- coding: cp1252 -*-
#movimento agora eh movimentos consumidos, a cada rodada o numero de movimentos aumentara 10, e as pecas vao consumir esses 10.
#cada peca pode se mover apenas uma vez, se clicar na peça e dps soltá-la em outra "casa" q n a inicial, contara como um movimento completo.
# 0 representa casa vazia

import math

class Tabuleiro:
    

    def __init__(self):
        self.tab = []
        
        

    def cria_tabuleiro(self):
       #deve ser inicializada no main game
        for i in [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]:
           self.tab.append(i)
        return self.tab[:]







class Pecas:#movimento agora eh movimentos consumidos

        #self.build_castelo = {'hp': 10000, 'defesa': 15, 'atq': 0, 'pontos_min_atq': 99999999, 'movimento': 0, 'alcance_max_atq': 0}
        #self.build_escudeiro = {'hp': 500, 'defesa': 150, 'atq': 100, 'pontos_min_atq': 1, 'movimento': 1, 'alcance_max_atq': 1}
        #self.build_general = {'hp': 1000, 'defesa': 50, 'atq': 400, 'pontos_min_atq': 1, 'movimento': 1, 'alcance_max_atq': 1}
        #self.build_arqueiro = {'hp': 500, 'defesa': 10, 'atq': 170, 'pontos_min_atq': 1, 'movimento': 1, 'alcance_max_atq': 3}
        #self.build_infantaria = {'hp': 600, 'defesa': 30, 'atq': 200, 'pontos_min_atq': 1, 'movimento': 1, 'alcance_max_atq': 1}
        #self.build_h_infantaria = {'hp': 700, 'defesa': 50, 'atq': 250, 'pontos_min_atq': 1, 'movimento': 1, 'alcance_max_atq': 1}
        #self.build_catapulta = {'hp': 400, 'defesa': 0, 'atq': 1000, 'pontos_min_atq': 5, 'movimento': 1, 'alcance_max_atq': 5}
        #self.build_cavalaria = {'hp': 700, 'defesa': 30,'atq': 200, 'pontos_min_atq': 1, 'movimento': 3, 'alcance_max_atq': 1}
        #self.build_h_cavalaria = {'hp': 800, 'defesa': 50, 'atq': 250, 'pontos_min_atq': 1, 'movimento': 2, 'alcance_max_atq': 1}

    def __init__(self, nome="",tipo="", jogador=""):
        #tentar tirar tipos daqui
        self.tipos = {'castelo' : [10000, 15, 0, 99999999, 99999999, 0], 'escudeiro' : [500, 150, 100, 1, 3, 1], 'general' : [1000, 50, 400, 1, 2, 1], 'arqueiro' : [500, 10, 170, 1, 2, 3], 'infantaria' : [600, 30, 200, 1, 2, 1], 'h_infantaria' : [700, 50, 250, 2, 3, 1], 'catapulta' : [400, 0, 1000, 3, 4, 5], 'cavalaria' : [700, 30, 200, 1, 1, 1], 'h_cavalaria' : [800, 50, 250, 2, 1, 1]}
        self.nome = nome
        self.tipo = tipo
        self.jogador = jogador 
        self.hp = self.tipos[tipo][0]              #hp
        self.defesa = self.tipos[tipo][1]          #defesa
        self.atq = self.tipos[tipo][2]             #atq
        self.pontos_min_atq = self.tipos[tipo][3]  #pontos_min_atq
        self.movimento = self.tipos[tipo][4]        #movimento
        self.alcance_max_atq = self.tipos[tipo][5] #alcance_max_atq





            

        
class Jogador:

    def __init__(self, nome="", jogador="1 or 2"):
    
        self.nome = str(nome)
        self.jogador = jogador
        self.pontos_atq = 1
        self.pontos_move = 10
        self.pecas = []
        self.vez = False
        


    def get_peca(self, peca):

        for pec in self.pecas:
            if pec.nome == peca:
                return pec



    def set_pecas(self): # está aparecendo no a. apos usar o set_pecas
         jogador = self.jogador
         self.castelo = Pecas("cas0", "castelo", jogador)
         self.escudeiro1 = Pecas("e1", "escudeiro", jogador)
         self.escudeiro2 = Pecas("e2", "escudeiro", jogador)
         self.general = Pecas("gen0", "general", jogador)
         self.arqueiro1 = Pecas("a1", "arqueiro", jogador)
         self.arqueiro2 = Pecas("a2", "arqueiro", jogador)
         self.arqueiro3 = Pecas("a3", "arqueiro", jogador)
         self.arqueiro4 = Pecas("a4", "arqueiro", jogador)
         self.infantaria1 = Pecas("i1", "infantaria", jogador)
         self.infantaria2 = Pecas("i2", "infantaria", jogador)
         self.infantaria3 = Pecas("i3", "infantaria", jogador)
         self.infantaria4 = Pecas("i4", "infantaria", jogador)
         self.h_infantaria1 = Pecas("h_i1", "h_infantaria", jogador)
         self.h_infantaria2 = Pecas("h_i2", "h_infantaria", jogador)
         self.catapulta1 = Pecas("cat1", "catapulta", jogador)
         self.catapulta2 = Pecas("cat2", "catapulta", jogador)
         self.cavalaria1 = Pecas("cav1", "cavalaria", jogador)
         self.cavalaria2 = Pecas("cav2", "cavalaria", jogador)
         self.h_cavalaria1 = Pecas("h_cav1", "h_cavalaria", jogador)
         self.h_cavalaria2 = Pecas("h_cav2", "h_cavalaria", jogador)
         #team = [castelo,escudeiro1, escudeiro2, general, arqueiro1, arqueiro2, arqueiro3, arqueiro4, infantaria1, infantaria2, infantaria3, infantaria4, h_infantaria1, h_infantaria2, catapulta1, catapulta2, cavalaria1, cavalaria2, h_cavalaria1, h_cavalaria2]
         self.pecas = [self.castelo, self.escudeiro1, self.escudeiro2, self.general, self.arqueiro1, self.arqueiro2, self.arqueiro3, self.arqueiro4, self.infantaria1, self.infantaria2, self.infantaria3, self.infantaria4, self.h_infantaria1, self.h_infantaria2, self.catapulta1, self.catapulta2, self.cavalaria1, self.cavalaria2, self.h_cavalaria1, self.h_cavalaria2]
         return True
    

    def posiciona_peca(self, peca, posicao="tupla do tipo (i,j)", tab="Matriz tabuleiro"):
        temp = self.get_peca(peca)
        i, j = posicao
        tab[i][j] = temp
        return True
        

    def move(self, p1="origem, tupla(i,j)", p2="destino, tupla(i,j)", tab="Matriz Tabuleiro"):
        oi, oj = p1
        di, dj = p2
        #n ha peças para mover
        if (tab[oi][oj] == 0) : 
            return False
        
        #destino vazio
        if tab[di][dj] == 0:
            #n_movimentos sera controlado pelo turno, aumentando x a cada turno.
            if tab[oi][oj].movimento <= self.pontos_move:
                if oi == di and abs(oj - dj) <= 1:
                    tab[di][dj] = tab[oi][oj]
                    tab[oi][oj] = 0
                    self.pontos_move -= tab[di][dj].movimento
                    return True
                
                if oj == dj and abs(oi - di) <= 1:
                    tab[di][dj] = tab[oi][oj]
                    tab[oi][oj] = 0
                    self.pontos_move -= tab[di][dj].movimento
                    return True

                if (oj != dj and oi != di) and (abs(oj - dj) <= 1 and abs(oi - di) <= 1):
                    tab[di][dj] = tab[oi][oj]
                    tab[oi][oj] = 0
                    self.pontos_move -= tab[di][dj].movimento
                    return True

        
        #existe alguma peça no destino
        if tab[di][dj] != 0 and tab[oi][oj].jogador != tab[di][dj].jogador:
            if oi == di and abs(oj - dj) <= tab[oi][oj].alcance_max_atq:
                if self.pontos_atq >= tab[oi][oj].pontos_min_atq:
                    self.ataque(tab[oi][oj], tab[di][dj])
                    self.pontos_atq -= tab[oi][oj].pontos_min_atq
                    if tab[di][dj].hp <= 0:
                        tab[di][dj] = 0
                        self.pontos_atq += 1
                    return 'atacou'
                
            if oj == dj and abs(oi - di) <= tab[oi][oj].alcance_max_atq:
                if self.pontos_atq >= tab[oi][oj].pontos_min_atq:
                    self.ataque(tab[oi][oj], tab[di][dj])
                    self.pontos_atq -= tab[oi][oj].pontos_min_atq
                    if tab[di][dj].hp <= 0:
                        tab[di][dj] = 0
                        self.pontos_atq += 1
                    return 'atacou'

            if (oj != dj and oi != di) and (abs(oj - dj) == abs(oi - di)) and abs(oj - dj) <= tab[oi][oj].alcance_max_atq and abs(oi - di) <= tab[oi][oj].alcance_max_atq:
                if self.pontos_atq >= tab[oi][oj].pontos_min_atq:
                    self.ataque(tab[oi][oj], tab[di][dj])
                    self.pontos_atq -= tab[oi][oj].pontos_min_atq
                    if tab[di][dj].hp <= 0:
                        tab[di][dj] = 0
                        self.pontos_atq += 1
                    return 'atacou'
                    
            if tab[di][dj].hp <= 0:
                tab[di][dj] = 0
                self.pontos_atq += 1
            return False



    def ataque(self, peca, enemy):
        enemy.hp -= (peca.atq - enemy.defesa)
        
        return True

    def end_turn(self, enemy):
        self.pontos_atq += 2
        self.pontos_move += 4
        self.vez = False
        enemy.vez = True
        
            


    

    
     
    

                                            
        
        
