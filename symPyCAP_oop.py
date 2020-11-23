# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:24:14 2020

@author: Katarina
"""
import sympy

class Solution(object):
    def __init__(self):
        self.number_of_nodes = 0
        self.node_currents = [] # J
        self.node_potentials = [] # V
        self.element_voltages = [] # JJ
        self.element_currents = [] # VV
        self.element_symbols = {} # ovo su simboli elemenata na osnovu 1. vrednosti iz liste 
        # to su R1, R2, Ug ....
        # prvi element ce uvek biti ta opsta vrednost   
        self.current_symbols = {} # ovo su I iz maksime 
    
    def __potential_symbol_definition(self):
        self.node_potentials = [sympy.symbols('V' + str(i)) for i in range(self.number_of_nodes)]
        
    def __make_MNA_equation(self, element):
        symbol = self.element_symbols[element[1]]
        
        if element[0] == 'R':
            node_A = element[2] # plus node
            node_B = element[3] # minus node
            R = symbol
            self.node_currents[node_A] += (self.node_potentials[node_A] - self.node_potentials[node_B]) / R
            self.node_currents[node_B] += (self.node_potentials[node_B] - self.node_potentials[node_A]) / R
            return True
    
        elif element[0] == 'V':
            node_A = element[2]
            node_B = element[3]
            Ug = symbol # ovo je simbol sa seme
            IUg = self.current_symbols[element[1]] # ovo je struja kroz generator. 
            # Ne treba da se izracuna struja kroz scaki element vec samo kroz generatore (i mozda jos nesto)
            # treba proveriri sa ilicem (ili u salexu za sta sve treba da se racuna)
    #        print(IUg)
            self.node_currents[node_A] += IUg
            self.node_currents[node_B] -= IUg 
            self.element_currents.append(self.node_potentials[node_A] - self.node_potentials[node_B] - Ug)
            self.element_voltages.append(IUg) # ovo mora da ide kao currents[symbol]
            return True

        elif element[0] == 'OpAmp':
            node_A = element[2][0]
            node_B = element[2][1]
            #dodati jednacine
        #elif dodoati i ostale elemente koji ne zahtevaju diferencijalne jednacine        
        else:
            return False
        #NEMAM RESENO STA SE DESAVA AKO JE STV NESTO FALSE->POGLEDAI SALECX ISTO
        
    def symPyCAP(self,element_list):
        #------------- Number of nodes ------------------
        nodes = {0} # ground node is always necessary
        for element in element_list:    
            print(element)
            
            if isinstance(element[2], list):
                nodes.add(element[2][0])
                nodes.add(element[2][1])
            else:
                nodes.add(element[2])
                nodes.add(element[3])
            
        self.number_of_nodes = max(nodes) + 1
        print("Number of nodes: " + str(self.number_of_nodes))
        
        #------------ Init of J = {0} and V to symbols Vi ----------------------
        self.node_currents = [0 for i in range(self.number_of_nodes)]
    
        # potentials of nodes: #NODE POTENTIAL SYMBOLS
        self.__potential_symbol_definition() # define Vi potentials 
        self.node_potentials[0] = 0 # potential of node 0 is equal to 0
        
        #-------------- Init of user defined symbols -----------------------

         
        for element in element_list:
            self.element_symbols[element[1]] = sympy.symbols(element[1])
        
        #-------------- I labels ALI ZASTO OVDE --------------------
        
        # dodavanje IUg u dictionary
        for element in element_list:
            if element[0] == 'V':
                self.current_symbols[element[1]] = sympy.symbols('I' + element[1])

        #------------- For every element in circuit, creating MNA equations -------
        result = map(self.__make_MNA_equation, element_list)
        print(list(result))
        
        equations = self.node_currents[1:self.number_of_nodes]
        for current_of_element in self.element_currents:
            equations.append(current_of_element)    
        print(equations)
        
        variables = self.node_potentials[1:self.number_of_nodes]
        for current in self.current_symbols: # iteriranje kroz dictionary i dodavanje u listu varijabli koje treba da se 
            # izracunaju
            variables.append(self.current_symbols[current]) # Treba da se ovde pristupa currents-ima a ne ovako direktno
        print(variables)
        
        solution = sympy.linsolve(equations, variables)
        return solution