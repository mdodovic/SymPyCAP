# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020
@authors: 
    Katarina Stanković (sk180183d@student.etf.bg.ac.rs)
    Matija Dodović (dm180072d@student.etf.bg.ac.rs)
"""
from symPyCAP_oop import Solution
from sympy import symbols


RLC = [
    ["V","E1",1,0],
    ["R","R1",1,2],
    ["L","L1",2,3],
    ["C","C1",3,0,"U0"]
]

circuit = Solution(RLC)

E, R, C, L, w = symbols('E,R,C,L,w')

solution = circuit.symPyCAP(omega = w, r = {"E1" : E, "R1" : R, "C1" : C, "L1" : L})

circuit.electric_circuit_specifications()
circuit.print_solutions()
circuit.print_specific_solutions()

print("With specific w:")

solution = circuit.symPyCAP(omega = 1/L/C, r = {"E1" : E, "R1" : R, "C1" : C, "L1" : L})

circuit.electric_circuit_specifications()
circuit.print_solutions()
circuit.print_specific_solutions()
