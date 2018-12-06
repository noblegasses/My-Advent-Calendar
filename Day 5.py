# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:45:31 2018

@author: coirn
"""

import Functions
chem = Functions.read_file("Day5list.txt")
done = False
chem_list = chem[0]
chem_list = list(chem_list)
chem_list.append(" ")
beta= []
totals=[]
counter = 0
popped=[]
alpha= [['B','b'],['A','a'],['C','c'],['D','d'],['E','e'],['F','f'],['G','g'],['H','h'],['I','i'],['L','l'],['M','m'],['N','n'],['O','o'],['P','p'],['Q','q'],['R','r'],['S','s'],['T','t'],['U','u'],['V','v'],['W','w'],['X','x'],['Y','y'],['Z','z']]
for a in range (len (alpha)):
    for x in range (len(chem_list)):
        if chem_list[x]==alpha[a][0] or chem_list[x]==alpha[a][1]:
            counter = counter +1 
    totals.append([alpha[a][0],counter])
    counter = 0
print (totals)
print (len(chem_list))
"""for a in range (len(alpha)):
    popped.append(chem_list)
    print (len (chem_list))
    print (len (popped[a])):"""
for a in range(len(alpha)):
    chem_list = chem[0]
    chem_list = list(chem_list)
    chem_list.append(" ")
    popped.append(chem_list)
    done=False
    counter = 0
    while True:
        for x in range(len(popped[a])):
                if popped[a][x]==alpha[a][0] or popped[a][x]==alpha[a][1]:
                    popped[a].pop(x)
                    #print(len(chem_list))
                    counter = counter +1
                    done = False
                    break
                else:
                    done = True
        if done == True:
            print("done removing: " + alpha[a][0]+', removed ' + str(counter) + " characters." )
            break
    counter = 0               
    done = False
    while True:
        for x in range(len(popped[a])):
            if x+1 < len(popped[a]):
                temp1 =popped[a][x].capitalize()
                temp2=popped[a][x+1].capitalize()
                if temp2==temp1 and popped[a][x] != popped[a][x+1]:
                    popped[a].pop(x+1)
                    popped[a].pop(x)
                    done = False
                    break
                else:
                    done = True
        if done == True:
            print("done processing: " + alpha[a][0], ", Polymer length is: " + str(len(popped[a])-1))
            break
    done = False
    popped[a] = ''.join(popped[a])
    beta.append([alpha[a][0],len(popped[a])-1])

beta.sort(key = lambda x: x[1])

#print(chem_list)
print(len(chem_list))
print(beta)