# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:44:31 2018

@author: coirn
"""
import numpy as N
import pandas as pd
serial = 4455
gridsize = 300
grid = N.empty((gridsize,gridsize))

def populate():
    for x in range(gridsize):
        for y in range(gridsize):
            power = x + 10
            power = power * y
            power = power + serial
            power = power * (x+10)
            power = int(str(power)[-3:-2])
            power = power - 5
            grid[x,y] = power
def sums():
    biggest = [0,[0,0],0]
    total = 0
    for z in range (gridsize):
        for x in range (gridsize-z):
            for y in range (gridsize-z):
                for a in range (z):
                    for b in range(z):
                        total = total + grid[x+a, y+b]
                if total > biggest[0]:
                    biggest[0] = total
                    biggest[1]=[x,y]
                    biggest[2]= z
                total = 0
    return biggest
populate()
maximium=sums()
print (maximium)
