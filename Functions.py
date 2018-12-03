# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:21:19 2018

@author: coirn
"""

#Functions needed for all the challenges
def read_file(filename): 
    try:
        f = open(filename, "r")
        number = f.read().split('\n')
        f.close()
        return number
    except Exception:
        print ("cannot read file")