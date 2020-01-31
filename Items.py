# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:02:58 2020

@author: Valentin Fenoux
"""
from random import randint

class Items :
    
    def __init__(self,coord) :
        self.coord = coord
        n = randint(0,2)
        Effect = ['health','strength','body']
        self.effect = Effect[n]
        
        