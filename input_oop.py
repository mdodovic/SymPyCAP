# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
"""
from symPyCAP_oop import Solution
"""
elements = [
            ["R", "R1", 2, 1],
            ["R", "R2", 1, 0],
            ["R", "R3", 1, 0],
            ["V", "Ug", 2, 0]          
            ]

system = Solution(elements)
solution = system.symPyCAP()
print(solution) # celokupno resenje u formi var: resenje(var), ...
print(solution['V1']) # pojedinacan pristup resenjima
print(solution['V2'])
print(solution['IUg'])
"""
"""
solution = system.symPyCAP([]) # Treba se odluciti
print(solution) # celokupno resenje u formi var: resenje(var), ...
print(solution['V1']) # pojedinacan pristup resenjima
print(solution['V2'])
print(solution['IUg'])
"""
Riordan_shema = [
    ["V", "Ug", 1, 0],
    ["OpAmp", "OpAmp1", [1,4], 5],
    ["R", "R1", 4, 0],
    ["R", "R2", 4, 5],
    ["R", "R3", 5, 2],
    ["OpAmp", "OpAmp2", [1,2], 3],
    ["R", "R4", 2, 3],
    ["R", "R5", 1, 3]
]

system = Solution(Riordan_shema)
solution = system.symPyCAP()
print(solution) # celokupno resenje u formi var: resenje(var), ...
print(solution['V1']) # pojedinacan pristup resenjima
print(solution['V2'])
print(solution['IUg'])
