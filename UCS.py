# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:04:56 2020

@author: mahbu
"""

from queue import PriorityQueue

Queue=PriorityQueue()

Graph = {}
pathcost = {}
parentNode = {}



Graph['A']= {'B':3,'G':1,'J':4}
Graph['B']= {'A':3,'D':10}
Graph['C']= {'H':3}
Graph['D']= {'B':10,'H':11,'J':3}
Graph['E']= {'F':2,'G':14,'I':1}
Graph['F'] = {'E':2,'G':8,'H':4,'I':2}
Graph['G']= {'A':1,'E':14,'F':8,'J':6}
Graph['H']= {'C':3,'D':11,'F':4,'I':6}
Graph['I']= {'E':1,'F':2,'H':6}
Graph['J']= {'A':4,'D':3,'G':6}


for elements in Graph:
    pathcost[elements]=100000;
    parentNode[elements]=None;

#as Queue is empty,we will push starting node in Q with a cost 0 
startingNode='A';


Queue.put((startingNode,0));

pathcost[startingNode]=0 #as it is the starting node it has no cost.

while not Queue.empty():
    
    check = Queue.get();
    value = check[1]; #storing the path cost of particular node
    for node,prevcost in Graph[check[0]].items():
        totalcost = value+prevcost;
        if(pathcost[node]>totalcost):
            pathcost[node]=totalcost;
            parentNode[node]=check[0];
            Queue.put((node,totalcost));
   
arr = []
goalNode='C';
while True:
   goalNode=parentNode[goalNode];
   if goalNode is None:
       break;
   arr.append(goalNode);
 
   
print(pathcost)
print(parentNode)
print("Path cost is :");
print(pathcost['C']);


arr.reverse();
arr.append('C');
print("Path traversed are: ")
print(arr);
    



            
    