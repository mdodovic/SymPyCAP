# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:24:14 2020
@author: Katarina
"""
import sympy

class Solution(object):
    def __init__(self, element_list):
        self.element_list = element_list
        self.number_of_nodes = 0
        self.node_currents = [] # J
        self.node_potentials = [] # V
        self.voltage_equations = [] # JJ
        self.current_variables = [] # VV
        self.element_symbols = {} # ovo su simboli elemenata na osnovu 1. vrednosti iz liste, opsta vrednost
        self.current_symbols = {} # ovo su I iz maksime STA CE NAM OVO
    
    def __potential_symbols_definition(self):
        self.node_potentials = [sympy.symbols('V' + str(i)) for i in range(self.number_of_nodes)]
        self.node_potentials[0] = 0 # potential of node 0 is equal to 0
        
    def __number_of_nodes(self):
        nodes = {0} # ground node is always necessary
        for element in self.element_list:    
            print(element)
            
            if isinstance(element[2], list):
                nodes.add(element[2][0])
                nodes.add(element[2][1])
            else:
                nodes.add(element[2])
                nodes.add(element[3])
            
        self.number_of_nodes = max(nodes) + 1
        print("Number of nodes: " + str(self.number_of_nodes))
        
    def __make_MNA_equation(self, element):
        type_of_element = element[0]
        symbol = self.element_symbols[element[1]]
        
        if type_of_element == 'R':
            node_A = element[2] # plus node
            node_B = element[3] # minus node
            R = symbol
            self.node_currents[node_A] += (self.node_potentials[node_A] - self.node_potentials[node_B]) / R
            self.node_currents[node_B] += (self.node_potentials[node_B] - self.node_potentials[node_A]) / R
            return True
    
        elif type_of_element == 'V':
            node_A = element[2]
            node_B = element[3]
            Ug = symbol # ovo je simbol sa seme
            IUg = sympy.symbols('I' + element[1]) # ovo je struja kroz generator. 
            # Ne treba da se izracuna struja kroz scaki element vec samo kroz generatore (i mozda jos nesto)
            # treba proveriri sa ilicem (ili u salexu za sta sve treba da se racuna)
    #        print(IUg)
            self.node_currents[node_A] += IUg
            self.node_currents[node_B] -= IUg 
            self.voltage_equations.append(self.node_potentials[node_A] - self.node_potentials[node_B] - Ug)
            self.current_variables.append(IUg) # ovo mora da ide kao currents[symbol]???
            return True

        elif type_of_element == 'OpAmp':
            node_A = element[2][0]
            node_B = element[2][1]
            #dodati jednacine
        #elif dodoati i ostale elemente koji ne zahtevaju diferencijalne jednacine        
        else:
            return False
        #NEMAM RESENO STA SE DESAVA AKO JE STV NESTO FALSE->POGLEDAI SALECX ISTO
        
    def symPyCAP(self):
        #------------- Number of nodes ------------------
        self.__number_of_nodes()
        
        #------------ Init of J = {0} and V to symbols Vi ----------------------
        self.node_currents = [0 for i in range(self.number_of_nodes)]
    
        # potentials of nodes: #NODE POTENTIAL SYMBOLS
        self.__potential_symbols_definition() # define Vi potentials 
        
        #-------------- Init of user defined symbols -----------------------

        for element in self.element_list:
            self.element_symbols[element[1]] = sympy.symbols(element[1])

        #------------- For every element in circuit, creating MNA equations -------
        result = map(self.__make_MNA_equation, self.element_list)
        print(list(result))
        
        equations = self.node_currents[1:self.number_of_nodes]
        equations.extend(self.voltage_equations)    
        print(equations)
        
        variables = self.node_potentials[1:self.number_of_nodes]
        variables.extend(self.current_variables)
        print(variables)
        
        solution = sympy.linsolve(equations, variables)
        return solution