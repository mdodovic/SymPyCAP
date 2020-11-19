# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:13:54 2020

@author: Matija
"""

import sympy 

E, R1, u1, i1 = sympy.symbols('E, R1, u1, i1')

equations = []
equations.append(E - R1 * i1)
equations.append(u1 - E)
variables = [i1, u1]
solution = sympy.solve(equations, variables)

print(solution)
print(solution[i1])
print(solution[u1])

import ahkab
#from ahkab import new_ac, run
#from ahkab.circuit import Circuit
#from ahkab.plotting import plot_results # calls matplotlib for you
