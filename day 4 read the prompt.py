# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:37:19 2018

@author: coirn
"""

import Functions
shifts = Functions.read_file("Day4list.txt")

chopped = []
gaurds = []
total= 0
i=0
for x in range (len(shifts)):
    chopped.append(shifts[x].split(" ", 1))
    chopped[x][0]= chopped[x][0].strip("[")
    chopped[x][1]= chopped[x][1].split("]")
    chopped[x][0]= chopped[x][0].split("-")
    chopped[x][1][0]= chopped[x][1][0].split(":")
    if chopped[x][1][1] == " falls asleep":
        chopped[x][1][1] = "s"
    elif chopped[x][1][1]==" wakes up":
        chopped[x][1][1]= "w"
    else:
        chopped[x][1][1] = chopped[x][1][1].strip (" Guard #")
        chopped[x][1][1] = chopped[x][1][1].strip (" begins shift")
chopped.sort()
for x in range (len(chopped)):
    if chopped [x][1][1]=="s":
        sleep = int(chopped[x][1][0][1])
    elif chopped [x][1][1]=="w":
        total = total + int(chopped[x][1][0][1]) - sleep
    else:
        current_gaurd = chopped[x][1][0][1]
        gaurds.append([current_gaurd,"placeholder"])
        gaurds[i][1] = total
        i= i+1
        total= 0
        
print (gaurd)