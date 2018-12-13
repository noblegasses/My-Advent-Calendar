# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:42:24 2018

@author: coirn
"""
######################Functions and setup#######################
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
    branches = [None for o in range(children)]
    Node(addr+1, metadata, branches)
    for x in range(children):
        for y in range (2):
            data[y] = licence[0]
            licence.pop(0)
        Write_Node(data [0],data[1])
    for x in range (metas):
        Node.add_metadata_values(nodes[addr], int(licence[0]),x)
        licence.pop(0)
def Find_Child_Addr(paddr):
    caddr = 1+paddr
    if len (nodes[paddr].children) != 0:
        for x in range (len(nodes[paddr].children)):
            Node.add_child_addr(nodes[paddr],caddr,x)
            caddr = Find_Child_Addr(caddr)
    return caddr
def Node_Value(addr,value):
    if len (nodes[addr].children) == 0:
        value=value+sum(nodes[addr].metadata)
    else:
        for x in range (len(nodes[addr].metadata)):
            if (nodes[addr].metadata[x] - 1) in range(len(nodes[addr].children)):
                value = Node_Value(nodes[addr].children[nodes[addr].metadata[x] - 1], value)
    return (value)
                
########################### Main Code #########################################
data=[0,0]
for y in range (2):
    data[y] = licence[0]
    licence.pop(0)
Write_Node(data [0],data[1])
Find_Child_Addr(0)
value = Node_Value(0,0)

for x in range(len (nodes)):
    sumtotal = sumtotal + sum(nodes[x].metadata)
print (value)