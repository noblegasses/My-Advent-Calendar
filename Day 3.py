# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:23:39 2018

@author: coirn
"""
import Functions
fabric = Functions.read_file("Day3list.txt")
chopped = []

def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)

for x in range (len(fabric)):
    chopped.append(fabric[x].split('@'))
    chopped[x][1] = chopped[x][1].split(":")
    chopped[x][1][0]=chopped[x][1][0].split(",")
    chopped[x][1][1]=chopped[x][1][1].split("x")
print (chopped)