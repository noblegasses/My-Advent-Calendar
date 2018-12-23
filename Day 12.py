# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:07:09 2018

@author: coirn
"""

import Functions as F
import copy as C
total = 0
allinfo=F.read_file("Day12list.txt")
#allinfo=F.read_file("debug12.txt")
allinfo[0] = allinfo[0].strip("initial state:")
state= C.deepcopy(allinfo[0])
state=list (state)
fullist = []
buffer= 10000
iterations= 131
total=[]
for x in range (len(state)+buffer*2):
    fullist.append('.')
for x in range (iterations):
    total.append(0)
fullist[buffer:-buffer]=state
state= C.deepcopy(fullist)
state1= C.deepcopy(fullist)
allinfo.pop(0)
allinfo.pop(0)
for x in range (len (allinfo)):
    allinfo[x]=allinfo[x].split(" => ")
    allinfo[x][0]=list(allinfo[x][0])
for a in range (iterations):
    match = 0
    for x in range(len(state)-5):
        for y in range(len(allinfo)):
            if state[x:x+5]== allinfo[y][0]:
                state1[x+2]= allinfo[y][1]
                match = 1
        if match == 0:
            state1[x+2]= '.'
        match = 0
    for z in range (len(state1)):
        if state1[z]=='#':
            total[a] = total[a] + z-buffer
    state = C.deepcopy(state1)
    #print (''.join(state1))
actual=C.deepcopy(total)
for x in range(len (total)-1):
    total[x+1] = total[x+1]- total[x]
N = ((50000000000)-124)/2
final=total[122]+total[123]+88*(2*N)
for x in range (len (actual)):
    actual[x]=  [x, actual[x]]
"""for x in range (len (total)):
    for y in range (len(total)):
        if x != y:
            if total[x] == total[y]:
                repeat.append([total[x],x])"""
print (actual)
print (final)
#print (''.join(state1))