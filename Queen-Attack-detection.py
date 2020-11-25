# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:53:13 2020

@author: mahbu
"""



           



Queen =[[0,0],[1,2],[2,4],[3,1],[4,3],[5,6],[6,4],[7,7]]


        



Board = [["q1",0,0,0,0,0,0,0],
         [0,0,"q2",0,0,0,0,0],
         [0,0,0,0,"q3",0,0,0],
         [0,"q4",0,0,0,0,0,0],
         [0,0,0,"q5",0,0,0,0],
         [0,0,0,0,0,0,"q6",0],
         [0,0,0,0,"q7",0,0,0],
         [0,0,0,0,0,0,0,"q8"]]

for i in range(8):
    Q=Queen[i]
    for j in range(8):
        if i==Q[0] and j==Q[1]:
            continue
        if Board[i][j] != 0:
            print("Row wise:",Board[i][j])
for i in range(8):
    
    for j in range(8):
        Q=Queen[j]
        if j==Q[0] and i==Q[1]:
            continue
        if Board[j][i] != 0:
            print("Column wise:",Board[j][i])
for i in range(8):
    Q=Queen[i]
    x=Q[0]
    y=Q[1]
    a=Q[0]
    b=Q[1]
    while 1:
        x=x+1
        y=y+1
        if x>7 or y > 7 or x < 0 or y < 0:
            break;
        if Board[x][y]!=0:
            print("Lower right diagonal of",Board[a][b]," is ",Board[x][y])

for i in range(8):
    Q=Queen[i]
    x=Q[0]
    y=Q[1]
    a=Q[0]
    b=Q[1]
    while 1:
        x=x+1
        y=y-1
        if x>7 or y > 7 or x < 0 or y < 0:
            break;
        if Board[x][y]!=0:
            print("Lower left diagonal of",Board[a][b]," is ",Board[x][y])

for i in range(8):
    Q=Queen[i]
    x=Q[0]
    y=Q[1]
    a=Q[0]
    b=Q[1]
    while 1:
        x=x-1
        y=y-1
        if x>7 or y > 7 or x < 0 or y < 0:
            break;
        if Board[x][y]!=0:
            print("Upper left diagonal of",Board[a][b]," is ",Board[x][y])

for i in range(8):
    Q=Queen[i]
    x=Q[0]
    y=Q[1]
    a=Q[0]
    b=Q[1]
    while 1:
        x=x-1
        y=y+1
        if x>7 or y > 7 or x < 0 or y < 0:
            break;
        if Board[x][y]!=0:
            print("Upper right diagonal of",Board[a][b]," is ",Board[x][y])
            
            

            
    