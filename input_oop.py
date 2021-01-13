# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
"""
from symPyCAP_oop import Solution
import sympy
import math

R = sympy.Symbol('R', real=True, positive=True)
W = sympy.symbols('W')


Wilkinson_shema = [
    ["V", "Vg", 4, 0],
    ["R", "R1", 1, 4],
    ["R", "R2", 2, 0],
    ["R", "R3", 3, 0],
    ["R", "R4", 2, 3],
    ["T", "T1", [1,0], [2,0], [math.sqrt(2)*R, math.pi/2]],
    ["T", "T2", [1,0], [3,0], [math.sqrt(2)*R, math.pi/2]]
]

system = Solution(Wilkinson_shema)
solution = system.symPyCAP(w=W, replacement = {"R1" : R, "R2" : R, "R3" : R, "R4" : 2*R})

system.print_specific_solutions()