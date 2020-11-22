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
            ["R", "R1", 2, 1],
            ["R", "R2", 1, 0],
            ["R", "R3", 1, 0],
            ["V", "Ug", 2, 0]          
            ]
    # Treba da se smisli u kojoj formi da se zadaje lista sa specificnim vrednostima elemenata
    # moj predlog
    # specific_solution = ["R1 = R", "R2 = 2R"]...
    solution = symPyCAP(elements)
    print(solution)
    #general_solution, specific_solution = symPyCAP(elements, specific_values_for_elements)
    #print(specific_solution)

# Itreriranje kroz listu 
#    for partial_solution in solution:
#        print(partial_solution)
#    for x in partial_solution:
#        print(x)

    """    
    riordan_shema = [
        ["V", "Ug", 1, 0, Ug],
        ["OpAmp", "OpAmp1", [1,4], 5],
        ["R", "R1", 4, 0, R1],
        ["C", "C2", 4, 5, C2],
        ["R", "R3", 5, 2, R3],
        ["OpAmp", "OpAmp2", [1,2], 3],
        ["R", "R4", 2, 3, R4],
        ["R", "R5", 1, 3, R5]
    ]
    """