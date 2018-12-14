# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:50:52 2018

@author: coirn
"""

import Functions as F
maxes = F.read_file("day9list.txt")
maxes = maxes[0].strip(" points")
maxes = maxes.split(" players; last marble is worth ")
maxplayers= int(maxes[0])
maxmarbles= int(maxes[1])*100
circle = [0]
player = []
[player.append(0) for i in range (maxplayers)]

def Turn(current=-1, ID=0, Marble=1):
    if ID==maxplayers:
        ID = 0
    if Marble%23 == 0:
        subtract= current -7
        if subtract != abs(subtract):
            subtract = len(circle) + subtract
        player[ID] =player[ID]+Marble+circle[subtract]
        circle.pop(subtract)
        current = subtract
    else:
        if current >= len (circle)-1:
            current = -1
        current += 2
        circle.insert(current,Marble)
    ID += 1
    Marble +=1
    info=[current, ID, Marble]
    return info
data = [-1, 0, 1]

while data[2]<= maxmarbles:
    data = Turn(data[0],data[1],data[2])

player.sort(reverse=True)
print (player[0])