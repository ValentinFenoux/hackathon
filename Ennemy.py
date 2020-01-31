# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:26:57 2020

@author: Utilisateur
"""
from random import random

def bouger_ennemy(Map, coord, di, dj):
    new_coord = np.array([coord[0]+di, coord[1]+dj])
    if deplacement_possible(Map, new_coord):
        coord = new_coord
    
def deplacement_possible(Map, coord):
    if Map[coord[0]][coord[1]] == "-" or Map[coord[0]][coord[1]] == "":
        return False
    else:
        return True
    
class Ennemy :
    """ Classe qui fournit toutes les caractéristiques des méchants"""

    def __init__(self, coord) :
        self.life = 15
        self.attack = 10
        self.body = 0
        self.luck = 0.7
        self.coord = coord
        
    def move(self, Map, coord_hero) :
        di = coord_hero[0] - self.coord[0]
        dj = coord_hero[1] - self.coord[1]
        if di > dj : 
            new_coord = bouger_ennemy(Map, self.coord, di/abs(di), 0)
            if new_coord == self.coord :
                self.coord = bouger_ennemy(Map, self.coord, 0, dj/abs(dj))
        else :
            new_coord = bouger_ennemy(Map, self.coord, 0, dj/abs(dj))
            if new_coord == self.coord :
                self.coord = bouger_ennemy(Map, self.coord, di/abs(di), 0)
            
            
        
    def E_attack(self, coord_hero, health_hero, body_hero) :
        if random() < 0.7 :
            health_hero -= self.attack - body_hero
            print(f"L'ennemi vous a enlevé {self.attack - body_hero} points de vie")
        return(health_hero)
            

        
        
    