# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:42:47 2018

@author: coirn
"""

import Functions as F
import copy as C
data = F.read_file("day10data.txt")
data=data[0]
data=data.strip("]")
data=data.strip("[")
data=data.split(", ")
datamod= C.deepcopy(data)
for x in range(len (data)):
    data[x]=int(data[x])
for x in range( len (data)-2):
    datamod[x+2] = data[x+2]- data[x]
for x in range (len (data)):
    datamod[x]=  [x, datamod[x]]
for x in range (len (data)):
    data[x]=  [x, data[x]]
print (datamod)
print (data)