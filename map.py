import numpy as np
import csv
import sys
import pygame
from pygame.locals import *
from random import randint
from math import sqrt
import itertools

pygame.init()

MAP1 = r'C:\Users\meri2\Documents\Mines_1A\PE\Maze\map1.txt'
MAP2 = r'C:\Users\meri2\Documents\Mines_1A\PE\Maze\map2.txt'
NUANCIER1 = color = {'': (0,0,0) , '.': (255,255,255), '-': (255,54,4), '#': (118,117,117), '@': (255, 255, 255), '=': (0,255,0), '+': (138,64,0)}
DIRECTION = {K_UP : (-1, 0), K_RIGHT : (0, 1), K_DOWN : (1, 0), K_LEFT : (0, -1)}
PLAYER_COLOR = (15, 15, 255)


def go():
    c = Carte(MAP2, 'rand')
    v = Game(c)
    v.loop()

def distance(l1, l2):
    acc = 0
    for i in range(len(l1)):
        acc += (l1[i] - l2[i])**2
    return acc

def draw_cell(screen, j, i, taille, color):
    lx = [(i+k) for k in range(0,taille)]
    ly = [(j+k) for k in range(0,taille)]
    for (i,j) in itertools.product(lx,ly):
        screen.set_at((i,j),color)
    return()

def rand_color(brightness = 255):
    return (randint(0,brightness), randint(0,brightness), randint(0,brightness))


def afficher(screen, matrice, nuancier, taille_pix):
    li, co = matrice.shape
    for (i, j) in itertools.product(range(li), range(co)):
        draw_pix(screen, nuancier[matrice[i, j]], i, j, taille_pix)

def draw_pix(screen, color, j, i, taille_pix):
    pygame.draw.rect(screen, color, Rect(i * taille_pix, j * taille_pix, taille_pix, taille_pix))
    return ()

def draw_fog(screen, j, i, taille_pix):
    """n = int(sqrt(taille_pix))
    lx = [(taille_pix*i+k) for k in range(0,taille_pix, n)]
    ly = [(taille_pix*j+k) for k in range(0,taille_pix, n)]
    for (i,j) in itertools.product(lx,ly):"""
    draw_pix(screen,rand_color(100), i, j, taille_pix)
    return ()

def rand_fog():
    g = randint(100,200)
    return (g, g, g)


class Carte():

    def __init__(self, chemin, nuance_mode = None):
        tabl = []    # Matrice pour créer la map
        fichier = open(chemin)
        csv_f = csv.reader(fichier, delimiter=';')
        for row in csv_f :
            tabl.append(row)
        fichier.close()
        self.data = np.array(tabl)
        i, j = self.get_player_position()
        self.discovered = self.mat_decouverte(i, j)
        if nuance_mode == 'rand':
            self.basic_nuancier()
        else:
            self.nuancier = NUANCIER1

    def basic_nuancier(self):
        present = set()
        li, co = self.data.shape
        for (i, j) in itertools.product(range(li), range(co)):
            if not(self.data[i, j] in present):
                present.add((self.data[i, j]))
        self.nuancier = {}
        for element in present:
            self.nuancier[element] = rand_color()
        self.nuancier['#'] = (240, 89, 67)

    def get_player_position(self):
        tampon = (self.data == '@')
        return np.nonzero(tampon)[0][0], np.nonzero(tampon)[1][0]

    def nuance(self, key):
        return self.nuancier[key]

    def get_status(self, i, j):
        return self.status[i, j]

    def mat_decouverte(self, i, j):
        mat_dec = np.zeros(self.data.shape, dtype=bool)
        while self.data[i - 1][j] != "-":
            i -= 1
        while self.data[i][j - 1] != "-":
            j -= 1
        i0, j0 = i, j
        while self.data[i][j + 1] != "-":
            j += 1
        j1 = j
        while self.data[i + 1][j] != "-":
            i += 1
        i1 = i
        for i in range(i0-1, i1 + 2):
            for j in range(j0-1, j1 + 2):
                mat_dec[i][j] = True
        return mat_dec


class Game():

    taille_pix = 12

    def __init__(self, carte, entity = []):
        self.map = carte
        self.li, self.co = self.map.data.shape
        self.entities = entity
        i, j = self.map.get_player_position()
        self.player = Personnage(j, i)

    def view(self):
        i, j = self.player.get_position()
        afficher(self.screen, self.map.data, self.map.nuancier, self.taille_pix)
        draw_pix(self.screen, PLAYER_COLOR, i, j, self.taille_pix)
        self.plot_fog()
        self.plot_health()
        pygame.display.update()

    def plot_health(self):
        left =

    def plot_fog(self):
        fogged = (self.map.discovered == False)
        indices = np.nonzero(fogged)
        for u in range(len(indices[0])):
            i, j = indices[0][u], indices[1][u]
            draw_fog(self.screen, j, i, self.taille_pix)

    def loop(self):
        self.screen = pygame.display.set_mode((self.co * self.taille_pix , self.li * self.taille_pix + 4*self.taille_pix))
        playing = True
        while playing:
            self.view()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    playing = False
                else:
                    self.interpret(event)
                    self.view()

    def interpret(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]:
                i, j = self.player.get_position()
                di, dj = DIRECTION[event.key]
                ni, nj = i + di, j + dj
                try:
                    if not(self.map.data[ni, nj] in ["-", ""]):
                        self.player.update_position(ni, nj)
                        self.revelation(ni, nj, di, dj)
                except:
                    return()

    def revelation(self, i,j, di, dj):
        if self.map.data[i, j] == "#":
            for direction in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                    ni = i + direction[0]
                    nj = j + direction[1]
                    if self.map.data[ni][nj] in ["#", "+"]:
                        self.map.discovered[ni, nj] = True
        elif self.map.data[i][j] == "+":
            wb = (self.map.data == ".") + (self.map.data =='-') + (self.map.data == '+')
            explored = np.zeros(wb.shape, dtype = bool)
            up, down, left, right = i, i, j, j
            pile = [(i, j)]
            while pile != []:
                (i, j) = pile.pop()
                if not(explored[i, j]):
                    explored[i, j] = True
                    if wb[i, j]:
                        if i > down: down = i
                        elif i < up: up = i
                        if j > right: right = j
                        elif j < left: left = j
                        for (di, dj) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            pile.append((i + di, j + dj))
            for i in range(up, down + 1):
                for j in range(left, right+1):
                    self.map.discovered[i, j] = True

class Personnage():

    def __init__(self, j, i):
        self.position = [i, j]
        self.inventory = set()
        self.update_stats()
        self.health = 100

    def update_stats(self):
        self.attack = 1
        self.armor = 0
        for item in self.inventory:
            self.attack += item.stat('attack')
            self.armor += item.stat('armor')

    def get_position(self):
        return self.position[0], self.position[1]

    def update_position(self, i, j):
        self.position = [i, j]


class Item():

    def __init__(self, name, graphique = None, effet = None):
        self.name = name
        if graphique == None:
            self.rand_graphique()
        if effet == None:
            self.rand_effet()

    def rand_graphique(self):
        pass

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
            new_coord = bouger_ennemy(Map, self.coord, int(di/abs(di)), 0)
            if new_coord == self.coord :
                self.coord = bouger_ennemy(Map, self.coord, 0, int(dj/abs(dj)))
        else :
            new_coord = bouger_ennemy(Map, self.coord, 0, int(dj/abs(dj)))
            if new_coord == self.coord :
                self.coord = bouger_ennemy(Map, self.coord, int(di/abs(di)), 0)
        if distance(self.coord, coord_hero) <= 2:
            return True

    def E_attack(self, coord_hero, health_hero, body_hero) :
        if random() < self.luck :
            health_hero -= self.attack - body_hero
            print(f"L'ennemi vous a enlevé {self.attack - body_hero} points de vie")
        return(health_hero)