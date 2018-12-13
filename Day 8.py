# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:42:24 2018

@author: coirn
"""

import Functions as F
licence = F.read_file("day8list.txt")
for x in range (len(licence)):
    licence = licence[x].split(" ")
sumtotal= 0
nodes=[]
class Node:
    def __init__(self, addr, metadata= [], children=None):
        self.addr= addr
        self.metadata = metadata
        self.children = children
        nodes.append(self)
    def __str__(self):
        return "Node: " + str(self.number)
    def add_child_addr(self, child, x):
        self.children[x] = child
    def add_metadata_values(self, datum, x):
        self.metadata[x]=datum
        

def Write_Node(children, metas):
    children = int(children)
    metas = int(metas)
    addr = len(nodes)
    data = [0,0]
    metadata=[None for i in range (metas)]
    #print (metadata)
    branches = [None for o in range(children)]
    Node(addr+1, metadata, branches)
    for x in range(children):
        for y in range (2):
            data[y] = licence[0]
            licence.pop(0)
        Write_Node(data [0],data[1])
    for x in range (children):
        Node.add_child_addr(nodes[addr],addr+x, x)
    for x in range (metas):
        Node.add_metadata_values(nodes[addr], int(licence[0]),x)
        licence.pop(0)

data=[0,0]
for y in range (2):
    data[y] = licence[0]
    licence.pop(0)
Write_Node(data [0],data[1])

for x in range(len (nodes)):
    sumtotal = sumtotal + sum(nodes[x].metadata)
print (sumtotal)