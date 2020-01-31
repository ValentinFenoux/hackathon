import pygame

import numpy as np

pygame.init()


def bouger_perso(map, coord, di, dj):
    new_coord = np.array(coord) + np.array([di, dj])
    if deplacement_possible(map, new_coord):
        coord = new_coord
    
def deplacement_possible(map, coord):
    if map[coord[0]][coord[1]] == "-" or map[coord[0]][coord[1]] == "¦":
        return False
    else:
        return True

running = True

map, coord

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
    bouger_perso(map, coord, di, dj)