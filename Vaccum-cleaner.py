# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:32:00 2020

@author: mahbu
"""

from random import randint
 



"""
we will take two rooms x and y. If x = 0 room is clean,x=1 then room is dirty
if y=0 room is clean if y=1 room is dirty

If vaccum_cleaner variable is 0 means it will clean the room ,
IF vaccum_cleaner variable is 1 means it will not clean the room

"""
def Count(x,y):
    cnt =0
    vaccum_cleaner = randint(0,1);
    print("vaccum_cleaner",vaccum_cleaner)
   
    if vaccum_cleaner == 0 and x == 1:
            cnt=cnt+1
    if vaccum_cleaner == 1 and x == 1:
            cnt=cnt-1
    if vaccum_cleaner == 0 and y == 1:
            cnt=cnt+1
    if vaccum_cleaner ==1 and y ==1:
            cnt=cnt-1
    if vaccum_cleaner == 1 and x == 0:
            cnt=cnt+0
            print("room is already clean")
    if vaccum_cleaner==1 and y == 0:
            cnt=cnt+0
            print("room is already clean")
    print("cnt is",cnt)
    return cnt

n=10   

add = 0
while n!=0:
    if n == 0:
        break;
    x = randint(0,1)
    if x == 0:
        print("room is clean")
    else:
        print("room is dirty")    
    y = randint(0,1)
    if y == 0:
        print("room is clean")
    else:
        print("room is dirty")    
    
    add=add+Count(x,y)
    n=n-1
    
print("Total ",add)
    
