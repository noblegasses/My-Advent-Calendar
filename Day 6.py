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
        if mat[x,y] == b'0':
            value = [0]
            distance = []
            [distance.append(value[:]) for x in range(len(coords))]
            Functions.alphabetize(distance)
            for z in range (len(coords)):
                distance[z][0]=abs (int(coords[z][1])-x) + abs (int(coords[z][0])-y)
            closest=[3500000,'v']
            for a in range(len(distance)):
                    if int (closest[0])>int(distance[a][0]):
                        closest = distance [a]
                    elif int (closest[0])==int(distance[a][0]):
                        closest[1] = "."
            mat[x,y] = closest[1].lower()
print(mat)
edges = []
print(mat.shape)
mat = mat.decode('utf-8')
for x in range(currentval[0]):
    repeat = 0
    for z in range(len(edges)):
        if mat[x,0] == edges[z]:
            repeat = 1
            break
    if repeat == 0:
        edges.append(mat[x,0])
for x in range(currentval[0]):
    repeat = 0
    for z in range(len(edges)):
        if mat[x,currentval[1]] == edges[z]:
            repeat = 1
            break
    if repeat == 0:
        edges.append(mat[x,currentval[1]])
for y in range(currentval[1]):
    repeat = 0
    for z in range(len(edges)):
        if mat[0,y] == edges[z]:
            repeat = 1
            break
    if repeat == 0:
        edges.append(mat[0,y])
for y in range(currentval[1]):
    repeat = 0
    for z in range(len(edges)):
        if mat[currentval[0],y] == edges[z]:
            repeat = 1
            break
    if repeat == 0:
        edges.append(mat[currentval[0],y])
        
totals = []
[totals.append(value[:]) for x in range(len(coords))]
Functions.alphabetize(totals)
for a in range (len(distance)):
    for x in range(currentval[0]+1):
        for y in range(currentval[1]+1):
            repeat = 0
            for z in range(len(edges)):
              if edges[z] == mat[x,y]:
                  repeat = 1
            if repeat == 0:
                if mat[x,y] == distance[a][1].lower(): #or mat[x,y] == distance[a][1]:
                    totals[a][0]=totals[a][0]+1
totals.sort(reverse = True)
        
            
            

print(edges)
print(totals)
print(mat.shape)
