# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
"""
from symPyCAP_oop import Circuit
import sympy
import math

# Konsultacije 0: Nevalidno kolo - nepostoji
V1V2 = [
       ["V", "E1", 1, 0],
       ["V", "E2", 1, 0]
       ]
circuit = Circuit(V1V2)

circuit.symPyCAP()
circuit.print_solutions()

#Kosnultacije 1: Nevalidno kolo - deljenje nulom


C,L = sympy.symbols('C,L')

LC_shema = [
    ["V","E1",1,0],
    ["C","C1",1,2],
    ["L","L1",2,0]
]
system = Circuit(LC_shema)
system.symPyCAP(w = 1/(sympy.sqrt(L*C)), replacement = {"C1" : C, "L1" : L})
system.print_specific_solutions()


# Kosnultacije 2: Vod sympy prosledjeno
R = sympy.Symbol('R', real=True, positive=True)
W = sympy.symbols('W')

Wilkinson_shema = [
    ["V", "Vg", 4, 0],
    ["R", "R1", 1, 4],
    ["R", "R2", 2, 0],
    ["R", "R3", 3, 0],
    ["R", "R4", 2, 3],
    ["T", "T1", [1,0], [2,0], [sympy.sqrt(2)*R, sympy.pi/2]],
    ["T", "T2", [1,0], [3,0], [sympy.sqrt(2)*R, sympy.pi/2]]
]

system = Circuit(Wilkinson_shema)
solution = system.symPyCAP(w=W, replacement = {"R1" : R, "R2" : R, "R3" : R, "R4" : 2*R})

system.print_specific_solutions()

