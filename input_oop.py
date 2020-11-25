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
"""

# Sabirac = [
#     ["V", "E1", 1, 0],
#     ["V", "E2", 2, 0],
#     ["V", "E3", 3, 0],
#     ["R", "R", 1, 5],
#     ["R", "R", 2, 5],
#     ["R", "R", 3, 5],
#     ["R", "R", 5, 4],
#     ["OpAmp", "OpAmp1", [0, 5], 4]
# ];
# system = Solution(Sabirac)
# solution = system.symPyCAP()
# for sol in solution:
#     print(sol,":",solution[str(sol)])

elements = [
["V","E1",7,6],
["R","R3",7,8],
["R","R2",6,3],
["R","R1",7,4],
["I","I2",8,5],
["I","I1",4,3],
["R","R4",5,4],
["R","R5",3,1],
["V","E2",0,4],
["V","E3",2,5],
["R","R6",1,0],
["R","R7",2,0]
]

system = Solution(elements)
solution = system.symPyCAP()
for key, value in solution.items():
    print(key, ":", value)


