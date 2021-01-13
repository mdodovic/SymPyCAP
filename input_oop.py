# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
"""
from symPyCAP_oop import Solution
import sympy
import math

#R = sympy.Symbol('R', real=True, positive=True)
#W = sympy.symbols('W')

#Wilkinson_shema = [
#    ["V", "Vg", 4, 0],
#    ["R", "R1", 1, 4],
#    ["R", "R2", 2, 0],
#    ["R", "R3", 3, 0],
#    ["R", "R4", 2, 3],
#    ["T", "T1", [1,0], [2,0], [math.sqrt(2)*R, math.pi/2]],
#    ["T", "T2", [1,0], [3,0], [math.sqrt(2)*R, math.pi/2]]
#]
#
#system = Solution(Wilkinson_shema)
#solution = system.symPyCAP(w=W, replacement = {"R1" : R, "R2" : R, "R3" : R, "R4" : 2*R})
#
#system.print_specific_solutions()
#Zc = sympy.Symbol('Zc', real=True, positive=True)
#tau = sympy.symbols('tau')
#
#
#TLine_shema = [
#    ["V", "Vg", 3, 0],
#    ["R", "R1", 3, 1],
#    ["T", "T1", [1,0], [2,0], [Zc,tau]],
#    ["R", "R2", 2, 0, "C0"]
#]
#
#
#system = Solution(TLine_shema)
#solution = system.symPyCAP(replacement = {"R1" : Zc, "R2" : Zc})
#system.print_specific_solutions()

T = [
       
       ["InductiveT","K1", [1, 0], [2, 0], ["L1", "L2", "L12"]],
       ["V","Vg", 3, 0],
       ["R","R1", 3, 1],
       ["R","R2", 2, 4],
       ["R","R3", 3, 4],       
       ]

L = sympy.Symbol('L', real=True, positive=True)

system = Solution(T)
system.symPyCAP()

system.symPyCAP(replacement = {"L1" : L, "L2" : L,"L12" : L})
system.print_specific_solutions()
#system.print_solutions()

