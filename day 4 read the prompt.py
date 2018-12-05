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
        gaurds[i-1][1] = int(gaurds[i-1][1])+total
        total= 0
    else:
        current_gaurd = chopped[x][1][1]
        gaurds.append([current_gaurd,0])
        i= i+1


gaurds.sort()
i=0
current_gaurd = gaurds[0][0]
gaurdtime = [[gaurds[0][0],0]]
for x in range (len(gaurds)):
    if gaurds[x][0] == current_gaurd:
        gaurdtime[i][1] = int(gaurdtime[i][1]) + int(gaurds[x][1])
    elif gaurds[x][0] != current_gaurd:
        current_gaurd = gaurds[x][0]
        gaurdtime.append(gaurds[x])
        i=i+1
        
gaurdtime.sort(key = lambda x: x[1],reverse= True)
i=0
timeschedule = []
tracking = False
target = gaurdtime[0][0] 
gaurdcheck= 0
for x in range (len(chopped)):
    if chopped[x][1][1] == target:
        if gaurdcheck == target:
            i=i+1
        gaurdcheck = chopped[x][1][1]
        tracking = True
        timeschedule.append([chopped[x+1][0],target,[]])
    if chopped[x][1][1] == 's' and tracking == True:
        sleep = chopped[x][1][0][1]
    if chopped[x][1][1] == 'w' and tracking == True:
        time = int (chopped[x][1][0][1]) - int (sleep)
        for y in range (time):
          timeschedule[i][2].append(y+int(sleep))
    if chopped[x][1][1] != target and chopped[x][1][1] !='w' and chopped[x][1][1] !='s' and tracking == True:
        tracking = False
        gaurdcheck = chopped[x][1][1]
        i= i + 1
frequency = []
for x in range (60):
    frequency.append([x,0])
    for y in range(len(timeschedule)):
        for z in range (len (timeschedule[y][2])):
            if x== timeschedule[y][2][z]:
                frequency[x][1] = int (frequency[x][1]) + 1
frequency.sort(key = lambda x: x[1],reverse= True)
#print (frequency)
#print (target)
gah = int(frequency [0][0]) * int(target)
print (gah)
#print (timeschedule)

#print ("\n\n\n\n\n\n")
#print (chopped)"""
#print (gaurdtime)
#print (chopped)
#print (gaurds)
counter = 0
"""for x in range (len (gaurds)):
    if chopped[x][0]== '5':
        counter = counter +1
print (counter)"""