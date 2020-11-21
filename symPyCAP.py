# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:29:58 2020

@author: Matija
"""

import sympy

Iug, Ug = sympy.symbols('Iug, Ug')

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
    
    node_currents = [] # J
    node_potentials = [] # V
    
    element_voltages = [] # JJ
    element_currents = [] # VV    

    node_currents = [0 for i in range(number_of_nodes)]
    
    # potentials of nodes:
    node_potentials = potential_symbol_definition(number_of_nodes) # define Vi potentials 
    node_potentials[0] = 0 # porential of node 0 is equal to 0
    
    for element in element_list:
        flag = make_MNA_equation(element, node_currents, node_potentials, currents, element_voltages, element_currents)
        if flag == False:
            return []
        
    equations = [node_currents[i] for i in range(1,number_of_nodes)]
    equations.append(element_currents[0])    
    print(equations)
    
    variables = [node_potentials[i] for i in range(1,number_of_nodes)]    
    variables.append(Iug)
    print(variables)
    
    solution = sympy.linsolve(equations, variables)
#    print(solution)
    
    return solution
            
def make_MNA_equation(element, node_currents, node_potentials, currents, element_voltages, element_currents):
    
    if element[0] == 'R':
        node_A = element[2] # plus node
        node_B = element[3] # minus node
        R = element[4]        
        node_currents[node_A] = node_currents[node_A] + (node_potentials[node_A] - node_potentials[node_B]) / R
        node_currents[node_B] = node_currents[node_B] + (node_potentials[node_B] - node_potentials[node_A]) / R
        return True

    elif element[0] == 'V':
        node_A = element[2]
        node_B = element[3]
        node_currents[node_A] = node_currents[node_A] + Iug
        node_currents[node_B] = node_currents[node_B] - Iug 
        element_currents.append(node_potentials[node_A] - node_potentials[node_B] - element[4])
        element_voltages.append(Iug)
        return True

    elif element[0] == 'OpAmp':
        node_A = element[2][0]
        node_B = element[2][1]
        # comment
        
    else:
        return False
        
