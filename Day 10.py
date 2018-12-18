# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:18:43 2018

@author: coirn
"""

import Functions as F
import numpy as N
import copy as C
import pandas as pd
data = F.read_file("day10list.txt")
position = []
velocity = []
past_position=[]
def setup():
    for x in range(len (data)):
        data [x] = data[x].strip("position=<")
        data [x] = data[x].strip(">")
        data[x] = data[x].split("> velocity=<")
        position.append(data[x][0])
        velocity.append(data[x][1])
        position[x] = position[x].split(', ')
        velocity[x] = velocity[x].split(', ')
        position[x][0] = int(position[x][0].strip(' '))
        velocity[x][0] = int(velocity[x][0].strip(' '))
        position[x][1] = int(position[x][1].strip(' '))
        velocity[x][1] = int(velocity[x][1].strip(' '))
def check_max_coords():
    maxvalues = [0,0]
    for x in range (len (position)):
        for y in range(len(maxvalues)):
            if position[x][y]>maxvalues[y]:
                maxvalues[y]=position[x][y]
    return maxvalues
def check_min_coords():
    minvalues = [0,0]
    for x in range (len (position)):
        for y in range(len(minvalues)):
            if position[x][y]<minvalues[y]:
                minvalues[y]=position[x][y]
    return minvalues
def move():
    global past_position
    past_position=C.deepcopy(position)
    for x in range(len(position)):
        for y in range(2):
            position [x][y] = position[x][y] + velocity[x][y]
    maxes = check_max_coords()
    return maxes
    
#def stars_align():
#    for x  in range()
setup()
limits = check_max_coords()
mins=check_min_coords()
prev_limits = C.deepcopy(limits)
prev_mins= C.deepcopy(mins)
seconds = 0
while limits <= prev_limits:
    seconds+=1
    prev_limits = C.deepcopy(limits)
    limits = move()
    prev_mins= C.deepcopy(mins)
    mins=check_min_coords()    
m=N.zeros((prev_limits[0]+1,prev_limits[1]+1))
for x in range(len(past_position)):
    m[(past_position[x][0]),(past_position[x][1])]=1
## convert your array into a dataframe
df = pd.DataFrame(m)

## save to xlsx file

filepath = r'C:\Users\coirn\Documents\Drill Project\Python\learning\coding challenges\My-Advent-Calendar\My-Advent-Calendar\starchart.xlsx'

df.to_excel(filepath, index=False)
print(seconds-1)
