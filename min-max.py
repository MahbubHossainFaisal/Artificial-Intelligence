# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 08:26:35 2020

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

#This code has not been completed


def Max_value(root):
    if not root['childs']:
        return root['value'];
    v=-math.inf;
    
    for action in root['childs']:
        v=max(v,Min_value(action));
        root['value']=v;
        return v;

def Min_value(root):
    if not root['childs']:
        return root['value'];
    v=math.inf;
    
    for action in root['childs']:
        v=min(v,Max_value(action));
        root['value']=v;
        return v;

    

Max_value(root);
print(root);






