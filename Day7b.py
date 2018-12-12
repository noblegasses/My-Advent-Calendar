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
       #busycheck = [workers[x].busy == False for x in range (len(workers))]
       if cycles>(1000000) == True:
           print ("help, im stuck at cleared")
           print (repeat)
           print (len(possiblities))
       if len (answer)== 0 or len(possiblities) == 0:
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
    while repeat==True:
        cycles +=1
        if cycles>100000:
           print ("help, im stuck at options")
           print (possibilities)
           print (step)
        if len(possibilities) == 0:
            break
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
def do_the_thing(answer,step):
    cycles = 0
    repeat= True
    while repeat == True:
        for y in range (len (answer)):
            cycles +=1
            if cycles>1000:
               print ("help, im stuck at do the thing step is "+str(len(step)))
            for x in range(len(step)):
                if step[x][0]==answer[y]:
                    step.pop(x)
                    repeat = True
                    break
                else: repeat = False
            if len(step)== 0:
                repeat = False
                break
    return step
            
workers=[]               
class Worker:
    def __init__(self, No, busy=False , task=None, time = None):
        self.number = No
        self.busy = busy 
        self.task = task
        self.time = time
        workers.append(self)
    def __str__(self):
        return "worker: " + str(self.number)
    def assign_job(self,task):
        self.task = task
        self.busy = True
    def finished_job(self):
        self.task = None
        self.busy = False
        self.time = None
    def timer(self, time):
        self.time = time
        

##################### Main Code #############################

elf1 = Worker(1)
elf2 = Worker(2)
elf3 = Worker(3)
elf4 = Worker(4)
elf5 = Worker(5)

step = prep()
possiblities=[]
possiblities[:] = F.alpha
answer=[]
processed=[]
[processed.append(0) for x in range(26)]
[answer.append(0) for x in range(26)]
inprogress= True
counter = 0
while True :
    possiblities[:] = F.alpha
    possiblities = cleared(processed, possiblities)
    possiblities = options (possiblities, step)
    #print("determined possible moves")
    for x in range(len (workers)):
        if workers[x].task == None and len (possiblities) != 0:
            Worker.assign_job(workers[x],possiblities[0])
            for y in range (len (F.alpha)):
                if possiblities[0] == F.alpha[y]:
                    Worker.timer(workers[x],(y+61))
            for z in range (len(processed)):
                if processed[z] == 0:
                    processed[z] = possiblities[0]
                    break
            possiblities.pop(0)
        if workers[x].time != None:
           Worker.timer(workers[x],(workers[x].time - 1))
        if workers[x].time != None and workers[x].time <= 0:
            for z in range (len(answer)):
                if answer[z]==0:
                    answer[z]= workers[x].task
                    break
            Worker.finished_job(workers[x])        
    step=do_the_thing(answer, step)      
    
    
    #print ("removed obstructing moves")
    #print (possiblities)
    counter += 1
    if counter > 1000000:
        print ("I may be stuck")
        print (answer)
        print (processed)
        busycheck = [workers[x].busy == False for x in range (len(workers))]
        print (step)
        
    if len(step)==0:
        break

for x in range(len (F.alpha)):
    for y in range (len (answer)):
        if answer[y] == F.alpha[x]:
            missingval= None
            pos = x
            break
        else:
            missingval = x
    if missingval!= None:
        answer[-1]=F.alpha[missingval]
        break
counter = counter + 60 + 4
print (counter)
answer = ''.join(answer)
print (answer)