# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:38:12 2020

@author: Valentin Fenoux
"""

"""Code pour la lecture de la carte"""

import csv
import numpy as np

def convertisseur(chemin) :
    tabl = []    # Matrice pour créer la map
    
    fichier = open(chemin)
    csv_f = csv.reader(fichier, delimiter=';')
    
    for row in csv_f :
        tabl.append(row)
    fichier.close()
    
    Map = np.array(tabl)
    return(Map)