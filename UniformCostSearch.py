# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:54:37 2020

@author: mahbu
"""

from queue import PriorityQueue
dict={
         'A':{'B':3,'J':4,'G':1}, 
         'B':{'A':3,'D':10},
         'J':{'A':4,'D':3,'G':6},
         'G':{'A':1,'J':6,'E':14,'F':8},
         'D':{'B':10,'H':11,'J':3},
         'E':{'G':14,'I':1,'F':2},
         'H':{'D':11,'F':4,'I':6,'C':3},
         'F':{'H':4,'G':8,'E':2,'I':2},
         'I':{'E':1,'F':2,'H':6},
         'C':{'H':3}
     }
path = {}
parent = {}
p = PriorityQueue()
for i in dict:
    parent[i]=None
    path[i]= 1e5
p.put((0,'A'))
path['A']=0
while not p.empty():
     u=p.get()
     cost=int(u[0])
     for i,j in dict[u[1]].items():
         w= cost+j
         if(path[i]>w):
             path[i]=w
             parent[i]=u[1]
             p.put((w,i))
print(path['C'])          
last='C'
while True:
    print(last)
    last=parent[last]
    if last is None:
        break


    