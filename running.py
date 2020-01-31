# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:17:07 2020

@author: Valentin Fenoux
"""

import sys
import pygame
from pygame.locals import *
import csv
import numpy as np
###-------------------- Fonction supplémentaire --------------------###

def convertisseur(chemin) :
    tabl = []    # Matrice pour créer la map
    
    fichier = open(chemin)
    csv_f = csv.reader(fichier, delimiter=';')
    
    for row in csv_f :
        tabl.append(row)
    fichier.close()
    
    Map = np.array(tabl)
    return(Map)
    
#----- Lecture de la carte ------#

Map = convertisseur(r"C:\Users\Utilisateur\Desktop\Python\hackathon\Map1.csv")

for i in len(Map)

# la taille du jeu en nombre de cellules
board_size = (len(Map[0,:]), len(Map[:,0]))
board_width, board_height = board_size

# la taille d'une cellule en nombre de pixels
size_pix = (20, 20)
pix_width, pix_height = size_pix

# On initialise pygame
pygame.init()

# Affichage de l'écran

screen = pygame.display.set_mode((board_width*pix_width, board_height*pix_height))

# Fonction pour le déplacement

def bouger_perso(Map, coord, di, dj):
    new_coord = np.array([coord[0]+di, coord[1]+dj])
    if deplacement_possible(Map, new_coord):
        coord = new_coord
    
def deplacement_possible(Map, coord):
    if Map[coord[0]][coord[1]] == "-" or Map[coord[0]][coord[1]] == "|" or Map[coord[0]][coord[1]] == " ":
        return False
    else:
        return True
    
# Affichage du jeu
color = {' ': (0,0,0) , '.': (255,255,255), '-': (255,54,4), '#': (118,117,117),
         '@': (255,255,255), '=': (0,255,0), '+': (138,64,0)}

# On initialise pygame
pygame.init()

# Affichage de l'écran

screen = pygame.display.set_mode((board_width*pix_width, board_height*pix_height))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        elif event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
            elif event.key == K_UP:
                di, dj = (-1, 0)
            elif event.key == K_RIGHT:
                di, dj = (0, 1)
            elif event.key == K_DOWN:
                di, dj = (1, 0)
            elif event.key == K_LEFT:
                di, dj = (0, -1)
    if di != 0 or dj != 0 :
        bouger_perso(Map, coord, di, dj)
        di, dj = (0, 0)