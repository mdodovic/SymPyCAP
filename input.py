# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:28:58 2020

@author: Matija
"""
from symPyCAP import symPyCAP

if __name__ == "__main__":
    
    #define simbols that are used
    
    #Ug, R1, R2, C2, R3, R4, R5 = sympy.symbols('Ug, R1, R2, C2, R3, R4, R5')
    """
    list = [ 
            ["R", "R1", 2, 1, R1],
            ["R", "R2", 1, 0, R2],
            ["R", "R3", 1, 0, R3],
            ["V", "Ug", 2, 0, Ug] 
            ]
    """
    elements = [
            ["R", "R", 2, 1],
            ["R", "R", 1, 0],
            ["R", "R", 1, 0],
            ["V", "Ug", 2, 0]          
            ]
    solution = symPyCAP(elements)
    print(solution)
