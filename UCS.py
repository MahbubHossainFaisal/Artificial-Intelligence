from queue import PriorityQueue
dictionary={
         'A':{'B':3,'J':4,'G':1}, 
         'B':{'A':3,'D':10},
         'C':{'H':3},
         'D':{'B':10,'H':11,'J':3},
         'E':{'G':14,'I':1,'F':2},
         'F':{'H':4,'G':8,'E':2,'I':2},
         'G':{'A':1,'J':6,'E':14,'F':8},
         'H':{'D':11,'F':4,'I':6,'C':3},
         'I':{'E':1,'F':2,'H':6},
         'J':{'A':4,'D':3,'G':6}
          
        
     }
node = []
parent = []
q = PriorityQueue()
for i in dictionary:
    parent[i]=None
    node[i]= 100000
    q.put('A')
while not q.empty():
     u=q.get()
#failed to do further