# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:11:53 2018

@author: coirn
"""

import Functions
def total_time(time):
    result = int(time[1][1])+int(time[1][0])*60
    result= result+ 60*(24*(int(time[0][2])))
    result= result + 60*(24*(30*int(time[0][1])))
    #result = result + (60*(24*(30*(12*int(time[0][0])))))
    return result

chopped = []
total = 0
i= 0
shifts = Functions.read_file("Day4list.txt")
#shifts = Functions.read_file("Debug4.txt")
for x in range (len(shifts)):
    chopped.append(shifts[x].split("]"))
    chopped[x][0]= chopped[x][0].split(" ")
    chopped[x][0][0]=chopped[x][0][0].strip("[")
    chopped[x][0][0]=chopped[x][0][0].split("-")
    chopped[x][0][1]=chopped[x][0][1].split(":")
    if chopped[x][1] == " falls asleep":
        chopped[x][1] = "s"
    elif chopped[x][1]==" wakes up":
        chopped[x][1]= "w"
    else:
        chopped[x][1] = chopped[x][1].strip (" Guard #")
        chopped[x][1] = chopped[x][1].strip (" begins shift")
    chopped[x][0]= total_time(chopped[x][0])
chopped.sort()
print (chopped)
gaurd=[]
totgaurd = []
current= "p"
counter = 0
for x in range (len (chopped)):
        if chopped[x][1] !='w' and chopped[x][1] !='s':
            gaurd.append([chopped[x][1],"placeholder"])
            i=i+1
        elif chopped[x][1] == 's':
            if chopped[x-1][1] != 's':
                startsleep = x
        elif chopped[x][1]=='w':
            if chopped[x-1][1]!= 'w':
                total = total + chopped[x][0] - chopped[startsleep][0]
        gaurd[i-1][1]=total
        total = 0

gaurd.sort() #key = lambda x: x[1],reverse = True
for x in range (len (gaurd)):
    if gaurd[x][0] != current:
        current = gaurd[x][0]
        totgaurd.append([gaurd[x][0],0])
        counter = counter +1
    totgaurd[counter-1][1]=totgaurd[counter-1][1]+gaurd[x][1] 
    
totgaurd.sort(key = lambda x: x[1],reverse = True)

print (gaurd)
print ("\n \n \n \n \n \n")
print (totgaurd)
print(final)          
            
#print (chopped)
