# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:11:53 2018

@author: coirn
"""

import Functions
def total_time(time):
    result = int(time[1][1]) + int(time[1][0]*60)
    result= result+ 60*(24*(int(time[0][2])+30*int(time[0][1])))
    result = result + (60*(24*(30*(12*int(time[0][0])))))
    return result

chopped = []

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
gaurd=[]
for x in range (len (chopped)):
        if chopped[x][1] != 'w' or 's':
            gaurd.append(chopped[x][1])
            i = chopped[x][1]
        elif chopped[x][1] == 's':
            if chopped[x-1][1] != 's':
                startsleep = x
        elif chopped[x][1]=='w':
            if chopped[x-1][1]!= 'w':
                gaurd[i][1]= total_time(chopped[x][0]) - total_time(chopped[startsleep][0])

test= int(total_time(chopped[2][0])) - int(total_time(chopped[1][0]))
print (test)          
            
#print (chopped)
