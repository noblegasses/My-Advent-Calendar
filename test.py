# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:07:38 2018

@author: coirn
"""
import Functions as F

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

elf = Worker(1)
possiblities = [] 
possiblities [:] = F.alpha
answer=[]
processed=[]
[processed.append(0) for x in range(26)]
[answer.append(0) for x in range(26)] 
looping = True
counter = 0
while looping == True :
    counter += 1
    if len(possiblities)== 0:
        break
    #print (counter)
    #print (len(workers))
    for x in range(len (workers)):
        print (workers[x].task)
        if workers[x].task == None and len (possiblities) != 0:
            Worker.assign_job(workers[x],possiblities[0])
            for y in range (len (F.alpha)):
                print(possiblities[0]==F.alpha[y])
                if possiblities[0] == F.alpha[y]:
                    Worker.timer(workers[x],(y+61))
                    print ("time " + str(1) + " = " + str(workers[0].time))
            for z in range (len(processed)):
                if processed[z] == 0:
                    processed[z] = possiblities[0]
                    break
            possiblities.pop(0)
        if workers[x].time != None:
           Worker.timer(workers[x],(workers[x].time - 1))
           print ("time " + str(1) + " = " + str(workers[0].time))
        if workers[x].time != None and workers[x].time <= 0:
            print ("time " + str(1) + " = " + str(workers[0].time))
            for z in range (len(answer)):
                if answer[z]==0:
                    answer[z]= workers[x].task
                    break
            Worker.finished_job(workers[x]) 
print (counter)
counter = counter + 26 + 60
print (counter)