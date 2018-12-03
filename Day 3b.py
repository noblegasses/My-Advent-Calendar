# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:23:39 2018

@author: coirn
"""
import Functions
import numpy
#import pandas as pd
fabric = Functions.read_file("Day3list.txt")
#fabric = Functions.read_file("debug3.txt")
chopped = []
total = []
for x in range (len(fabric)):
    chopped.append(fabric[x].split('@'))
    chopped[x][1] = chopped[x][1].split(":")
    chopped[x][1][0]=chopped[x][1][0].split(",")
    chopped[x][1][1]=chopped[x][1][1].split("x")
    chopped[x][1][0][0] = int(chopped[x][1][0][0])
    chopped[x][1][0][1] = int(chopped[x][1][0][1])
    chopped[x][1][1][0] = int(chopped[x][1][1][0])
    chopped[x][1][1][1] = int(chopped[x][1][1][1])
size = 1020
sheet = numpy.zeros(shape=(size,size))

for a in range (len(chopped)):
    for x in range (int(chopped[a][1][1][1])):
        for y in range (int (chopped[a][1][1][0])):
            if sheet[x+chopped[a][1][0][1], y+chopped[a][1][0][0]] == 0:
                sheet[x+chopped[a][1][0][1], y+chopped[a][1][0][0]] = a
            elif sheet[x+chopped[a][1][0][1], y+chopped[a][1][0][0]] != 0:
                sheet[x+chopped[a][1][0][1], y+chopped[a][1][0][0]] = 20000

"""## convert your array into a dataframe
df = pd.DataFrame (sheet)

## save to xlsx file

filepath = 'sheet.xlsx'

df.to_excel(filepath, index=False)"""

print (str(sheet))
for a in range (len(chopped)):
    total.append(0)
    for x in range (size):
        for y in range (size):
            if sheet.item((x,y)) == a:
                total[a] = total[a] + 1
    if total [a]== chopped[a][1][1][1] * chopped[a][1][1][0]:
        print (total[a])
        choppedtotal= (chopped[a][1][1][1] * chopped[a][1][1][0])
        print (str(chopped[a][1][1][1])+' * '+str(chopped[a][1][1][0])+ ' = ' + str(choppedtotal))
        ans = chopped[a][0]
        break
print (ans)