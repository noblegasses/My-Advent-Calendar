# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:06:37 2018

@author: coirn
"""
################### Imports and Functions ###################
import Functions as F
def prep():#prepare the data for use
    steps= F.read_file("Day7list.txt")
    for x in range(len(steps)):
        steps[x] = steps[x][5:]
        steps[x] = steps[x].strip(' can begin.')
        steps[x] = steps[x].split(' must be finished before step ')
        
    return(steps)
    
def cleared(answer, possiblities):#removes items from the check list that have already been used
    cycles= 0
    repeat= True
    while repeat==True:
       cycles +=1
       if cycles>len(possiblities):
           print ("help, im stuck at cleared")
       if len (answer)== 0:
           repeat= False 
       for y in range (len(answer)): 
            for x in range (len(possiblities)):
                if answer[y]==possiblities[x]:
                    possiblities.pop(x)
                    repeat = True
                    break
                else:
                    repeat = False
       if repeat == False:
        break
    return possiblities
def options(possibilities,step):
    cycles = 0
    repeat= True
    while True:
        cycles +=1
        if cycles>len(step):
           print ("help, im stuck at options")
           print (possibilities)
           print (step)
        for x in range(len (step)):
            for y in range(len (possibilities)):
                if step[x][1]== possibilities[y]:
                    possibilities.pop(y)
                    repeat = True
                    break
                else:
                    repeat= False
        if repeat == False:
            break
    possibilities.sort()
    return(possibilities)
def do_the_thing(possiblities,step):
    cycles = 0
    repeat= True
    while repeat == True:
        cycles +=1
        if cycles>1000:
           print ("help, im stuck at do the thing step is "+str(len(step)))
        for x in range(len(step)):
            if step[x][0]==possiblities[0]:
                step.pop(x)
                repeat = True
                break
            else: repeat = False
        if len(step)== 0:
            repeat = False
            break
    return step
            
                
                    

##################### Main Code #############################

step = prep()
possiblities=[]
possiblities[:] = F.alpha
answer=[]
[answer.append(0) for x in range(26)]

inprogress= True
counter = 0
for x in range(25):
    possiblities[:] = F.alpha
    possiblities = cleared(answer, possiblities)
    print("removed excess items")
    possiblities = options (possiblities, step)
    print (possiblities)
    print("determined possible moves")
    answer[x]=possiblities[0]
    step=do_the_thing(possiblities, step)
    print ("removed obstructing moves")
    counter += 1

for x in range(len (F.alpha)):
    for y in range (len (answer)):
        if answer[y] == F.alpha[x]:
            missingval= None
            break
        else:
            missingval = x
    if missingval!= None:
        answer[-1]=F.alpha[missingval]
print (answer)
answer = ''.join(answer)
print (answer)
