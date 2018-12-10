# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:29:47 2018

@author: coirn
"""

import Functions
import numpy


coords = Functions.read_file("Day6list.txt")
#coords = Functions.read_file("debug6.txt")
coords=[coords[x].split(", ") for x in range(len(coords))]
currentval = [0,0]
for y in range (len(coords[0])):
    for x in range (len (coords)):
        if int(coords[x][y])>int(currentval[y]):
            currentval[y]=int(coords[x][y])
currentval[0] = currentval[0] + 1
currentval[1] = currentval[1] + 1 
currentval=currentval[::-1]      
print(currentval)  
Functions.alphabetize(coords)
mat=numpy.chararray([currentval[0]+1,currentval[1]+1], itemsize=2)
mat[:]= "0"
for x in range (len(coords)):
    #mat[5,0]='A'
    mat[int(coords[x][1]),int(coords[x][0])]=coords[x][2]
print(mat)
for x in range(currentval[0]+1):
    for y in range (currentval[1]+1):
        value = [0]
        distance = []
        [distance.append(value[:]) for x in range(len(coords))]
        Functions.alphabetize(distance)
        for z in range (len(coords)):
            distance[z][0]=abs (int(coords[z][1])-x) + abs (int(coords[z][0])-y)
        tot = 0
        for z in range(len(distance)):
            tot = tot + distance[z][0]
        if tot < 10000 :
            mat[x][y]= 'y'
        else:
            mat[x][y]= 'n'
print(mat)
total = 0
mat= mat.decode('utf-8')
for x in range(currentval[0]+1):
    for y in range(currentval[1]+1):
        if mat[x,y] == 'y':
            total = total+1
print (total)
        