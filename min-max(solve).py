# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:01:44 2020

@author: mahbu
"""

import math
root = {"value":"" ,
        "childs": [
            {"value": "",
             "childs":[
                    {"value": 5, "childs":[]},
                    {"value": 3, "childs":[]},
                    {"value": 9, "childs":[]}
                    ]
             },
            {"value": "",
             "childs":[
                    {"value": 2, "childs":[]},
                    {"value": 8, "childs":[]}
                    
                    ]
             }
            ]
        }


def Max_value(root):
    if not root['childs']:
        return root['value'];
    v=-math.inf;
    
    for action in root['childs']:
        v=max(v,Min_value(action));
        root['value']=v;
    return v;               #Changed here

 

def Min_value(root):
    if not root['childs']:
        return root['value'];
    v=math.inf;
    
    for action in root['childs']:
        v=min(v,Max_value(action));
        root['value']=v;
    return v;            #changed here


result = Min_value(root);    # Changed here
print(result);

print(root);