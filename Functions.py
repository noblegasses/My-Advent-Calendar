# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:21:19 2018

@author: coirn
"""
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Functions needed for all the challenges
def read_file(filename): 
    try:
        f = open(filename, "r")
        number = f.read().split('\n')
        f.close()
        return number
    except Exception:
        print ("cannot read file")
        
def alphabetize(info):
    
    for x in range(len(info)):
        temp=[]
        if(int(x/26)>0):
            temp.append(alpha[int(x/26)-1])
        temp.append(alpha[x%26])
        temp = ''.join(temp)
        info[x].append(temp)
    return info