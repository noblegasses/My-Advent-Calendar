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
alpha= [['A','a'],['B','b'],['C','c'],['D','d'],['E','e'],['F','f'],['G','g'],['H','h'],['I','i'],['L','l'],['M','m'],['N','n'],['O','o'],['P','p'],['Q','q'],['R','r'],['S','s'],['T','t'],['U','u'],['V','v'],['W','w'],['X','x'],['Y','y'],['Z','z']]

for a in range(len(alpha)):
    popped=chem_list
    while True:
        for x in range(len(popped)):
                if popped[x]==alpha[a][0] or popped[x]==alpha[a][1]:
                    popped.pop(x)
                    done = False
                    break
                else:
                    done = True
        if done == True:
            print("done removing: " + alpha[a][0])
            break
                    
    done = False
    while True:
        for x in range(len(popped)):
            if x+1 < len(popped):
                temp1 =popped[x].capitalize()
                temp2=popped[x+1].capitalize()
                if temp2==temp1 and popped[x] != popped[x+1]:
                    popped.pop(x+1)
                    popped.pop(x)
                    done = False
                    break
                else:
                    done = True
        if done == True:
            print("done processing: " + alpha[a][0])
            break
    done = False
    popped = ''.join(popped)
    beta.append([alpha[a][0],len(popped)-1])
beta.sort(key = lambda x: x[1])

print(chem_list)
print(len(chem_list))
print(beta)