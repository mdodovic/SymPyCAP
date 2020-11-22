# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:29:58 2020

@author: Matija
"""

import sympy

Iug = sympy.symbols('Iug')

def potential_symbol_definition(n):
    list_of_potential_symbols = ['V' + str(i) for i in range(n)]
    for i in range(len(list_of_potential_symbols)):
        list_of_potential_symbols[i] = sympy.symbols(list_of_potential_symbols[i])
    return list_of_potential_symbols

def symPyCAP(element_list):
        
    number_of_nodes = 0
    
    nodes = {0} # ground node is always necessary
    for element in element_list:    
        print(element)
        
        if isinstance(element[2], list):
            nodes.add(element[2][0])
            nodes.add(element[2][1])
        else:
            nodes.add(element[2])
            nodes.add(element[3])
        
    number_of_nodes = max(nodes) + 1
    print("Number of nodes: " + str(number_of_nodes))
    
    currents = [] # I 
    #Napraviti da se ovde currents-u pristupa preko elemenata
    
    node_currents = [] # J
    node_potentials = [] # V
    
    element_voltages = [] # JJ
    element_currents = [] # VV    

    node_currents = [0 for i in range(number_of_nodes)]
    
    # potentials of nodes:
    node_potentials = potential_symbol_definition(number_of_nodes) # define Vi potentials 
    node_potentials[0] = 0 # porential of node 0 is equal to 0

    element_symbols = {} # ovo su simboli elemenata na osnovu 1. vrednosti iz liste 
    # to su R1, R2, Ug ....
    # prvi element ce uvek biti ta opsta vrednost    
    for element in element_list:
        element_symbols[element[1]] = sympy.symbols(element[1])
    

    
    for element in element_list:
        flag = make_MNA_equation(element, element_symbols[element[1]], node_currents, node_potentials, currents, element_voltages, element_currents)
        if flag == False:
            return []
        
    equations = node_currents[1:number_of_nodes]
    for current_of_element in element_currents:
        equations.append(current_of_element)    
    print(equations)
    
    variables = node_potentials[1:number_of_nodes]
    variables.append(Iug) # Treba da se ovde pristupa currents-ima a ne ovako direktno
    print(variables)
    
    solution = sympy.linsolve(equations, variables)
#    print(solution)
    
    return solution
            
def make_MNA_equation(element, symbol, node_currents, node_potentials, currents, element_voltages, element_currents):
    
    if element[0] == 'R':
        node_A = element[2] # plus node
        node_B = element[3] # minus node
        R = symbol
        node_currents[node_A] = node_currents[node_A] + (node_potentials[node_A] - node_potentials[node_B]) / R
        node_currents[node_B] = node_currents[node_B] + (node_potentials[node_B] - node_potentials[node_A]) / R
        return True

    elif element[0] == 'V':
        node_A = element[2]
        node_B = element[3]
        node_currents[node_A] = node_currents[node_A] + Iug
        node_currents[node_B] = node_currents[node_B] - Iug 
        Ug = symbol
        element_currents.append(node_potentials[node_A] - node_potentials[node_B] - Ug)
        element_voltages.append(Iug) # ovo mora da ide kao currents[symbol]
        return True

    elif element[0] == 'OpAmp':
        node_A = element[2][0]
        node_B = element[2][1]
        #dodati jednacine
        
    else:
        return False
        
