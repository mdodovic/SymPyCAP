# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
"""
from symPyCAP_oop import Solution

elements = [
            ["R", "R1", 2, 1],
            ["R", "R2", 1, 0],
            ["R", "R3", 1, 0],
            ["V", "Ug", 2, 0]          
            ]

system = Solution(elements)
print(system.symPyCAP())



