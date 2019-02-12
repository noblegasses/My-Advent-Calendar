# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:08:12 2018

@author: coirn
"""

import Functions as F

tracks = F.read_file("day13list.txt")
#tracks = F.read_file("debug13.txt")
for x in range(len(tracks)):
    tracks[x] = [z for z in tracks[x]] 
    
up = '^'
down = 'v'
left = '<'
right = '>'
turns=['/','\\']
xy=[0,1]
directions=[up,down,left,right]
crash = False
def takeSecond(elem):
    return elem[1]
def initpos():
    positions=[]
    for x in range(len (tracks)):
        for y in range(len(tracks[x])):
            if (tracks [x][y]== left) or (tracks [x][y] == right) or (tracks [x][y]== up) or (tracks [x][y]== down):
                positions.append([tracks[x][y],[x,y],0])
                if tracks [x][y]== left or tracks [x][y] == right:
                    tracks [x][y] = '-'
                if tracks [x][y]== up or tracks [x][y] == down:
                    tracks [x][y] = '|' 
    return positions
carts =initpos()
def move():
    collision = False
    #print (carts)
    #print ("\n")
    for x in range ( len (carts)):
        #print (carts[x][1])
        if carts[x][0]== left and tracks[carts[x][1][0]][carts[x][1][1]]== '/':
            #print ('old direction ' + carts[x][0] + " " + turns [0])
            carts[x][0] = down
            #print ('changed ' +str(x)+carts[x][0]) 
        elif carts[x][0]== right and tracks[carts[x][1][0]][carts[x][1][1]]== '/':
            #print ('old direction ' + carts[x][0] + " " + turns[0])
            carts[x][0] = up
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== left and tracks[carts[x][1][0]][carts[x][1][1]]== '\\':
            #print ('old direction ' + carts[x][0] + " " + turns[1])
            carts[x][0] = up
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== right and tracks[carts[x][1][0]][carts[x][1][1]]== '\\':
            #print ('old direction ' + carts[x][0] + " " + turns[1])
            carts[x][0] = down 
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== up and tracks[carts[x][1][0]][carts[x][1][1]]== '/':
            #print ('old direction ' + carts[x][0] + " " + turns[0])
            carts[x][0] = right
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== down and tracks[carts[x][1][0]][carts[x][1][1]]== '/':
            #print ('old direction ' + carts[x][0] + ' ' + turns [0])
            carts[x][0] = left
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== up and tracks[carts[x][1][0]][carts[x][1][1]]== '\\':
            #print ('old direction ' + carts[x][0] + ' ' + turns[1])
            carts[x][0] = left
            #print ('changed ' +str(x)+carts[x][0])
        elif carts[x][0]== down and tracks[carts[x][1][0]][carts[x][1][1]]== '\\':
            #print ('old direction ' + carts[x][0]+ ' ' + turns[1])
            carts[x][0] = right
            #print ('changed ' +str(x)+carts[x][0])
        elif tracks[carts[x][1][0]][carts[x][1][1]]== '+':
            if carts[x][2]==0:
                carts[x][2]=1
                if carts[x][0]==up:
                    carts[x][0]=left
                elif carts[x][0]==right:
                    carts[x][0]=up
                elif carts[x][0]==down:
                    carts[x][0]=right
                elif carts[x][0]==left:
                    carts[x][0]=down
            elif carts[x][2]==1:
                carts[x][2]= 2
            elif carts[x][2]==2:
                carts[x][2]=0
                if carts[x][0]==up:
                    carts[x][0]=right
                elif carts[x][0]==right:
                    carts[x][0]=down
                elif carts[x][0]==down:
                    carts[x][0]=left
                elif carts[x][0]==left:
                    carts[x][0]=up
        
        #print(str(x)+ " " +carts[x][0]+ str(carts[x][1]))
        if carts[x][0]== left:
            carts[x][1][1]-= 1
        if carts[x][0]== right:
            carts[x][1][1]+= 1
        if carts[x][0]== down:
            carts[x][1][0]+= 1
        if carts[x][0]== up:
            carts[x][1][0]-= 1
        #if tracks[carts[x][1][0]][carts[x][1][1]] ==' ':
            #print ("derailed!!!")
        #print(str(x)+ " " +carts[x][0]+ str(carts[x][1]))
        for z in range (len (carts)):
            for y in range (len(carts)):
                if z != y:
                    if carts[z][1] == carts[y][1]:
                        collision = [carts [z][1],[x,y]]
                        break
            if collision != False:
                break
        if collision != False:
                break
    carts.sort(key= takeSecond)
    return collision

        
#print (str(len(tracks)) +" "+ str(len(tracks[0])))

counter = 0
while len(carts) > 1:
    counter +=1
    crash = move()
    print(crash)
    if crash!= False:
        carts.pop(crash[1][0])
        carts.pop(crash[1][1])
print (counter)
print (carts)   