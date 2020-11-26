# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:24:14 2020
@author: Katarina
"""
import sympy

class Solution(object):
    def __init__(self, element_list):
        self.element_list = element_list
        self.number_of_nodes = self.__number_of_nodes()
        self.node_currents = [] # J
        self.node_potentials = [] # V
        self.voltage_equations = [] # JJ
        self.current_variables = [] # VV
        self.element_symbols = {} # electric circuit symbols
        
        self.equations = []
        self.variables = []
        
        self.time_domain = False
        
        self.solution = {}       
        
    def __node_currents_init(self):
        self.node_currents = [0 for i in range(self.number_of_nodes)]
    
    def __potential_symbols_definition(self):
        self.node_potentials = [sympy.symbols('V' + str(i)) for i in range(self.number_of_nodes)]
        self.node_potentials[0] = 0 # potential of node 0 is equal to 0
        
    def __number_of_nodes(self):
        """
        set number of nodes to maximum node from electric circuit increased by 1
        """
        nodes = {0} # ground node is always necessary
        for element in self.element_list:    
            # print(element)
            
            if isinstance(element[2], list):
                nodes.add(element[2][0])
                nodes.add(element[2][1])
            else:
                nodes.add(element[2])
                nodes.add(element[3])
            
        return max(nodes) + 1
        
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
            Ug = symbol 
            IUg = sympy.symbols('I' + element[1]) # ovo je struja kroz generator. 
            # Ne treba da se izracuna struja kroz scaki element vec samo kroz generatore (i mozda jos nesto)
            # treba proveriri sa ilicem (ili u salexu za sta sve treba da se racuna)
            #print(IUg)
            self.node_currents[node_A] += IUg
            self.node_currents[node_B] -= IUg 
            self.voltage_equations.append(self.node_potentials[node_A] - self.node_potentials[node_B] - Ug)
            self.current_variables.append(IUg)
            return True

        elif type_of_element == 'OpAmp':
            node_A1 = element[2][0]
            node_A2 = element[2][1]
            node_B = element[3]

            IOpAmp = sympy.symbols('I' + element[1])  

            self.node_currents[node_B] += IOpAmp
            self.voltage_equations.append(self.node_potentials[node_A1] - self.node_potentials[node_A2])
            self.current_variables.append(IOpAmp)
            return True
        
        elif type_of_element == 'I':
            node_A = element[2]
            node_B = element[3]
            Ig = symbol
            self.node_currents[node_A] += Ig
            self.node_currents[node_B] -= Ig 
            return True
        
        elif type_of_element == 'VCVS':
            node_A1 = element[2][0]
            node_A2 = element[2][1]
            node_B1 = element[3][0]
            node_B2 = element[3][1]
            amplification = sympy.symbols(str(element[4])) #razmatranje
            I2 = sympy.symbols('I' + element[1])
            self.node_currents[node_B1] += I2
            self.node_currents[node_B2] -= I2
            eq = self.node_potentials[node_B1] - self.node_potentials[node_B2] - \
                amplification * (self.node_potentials[node_A1] - self.node_potentials[node_A2])
            self.voltage_equations.append(eq)
            self.current_variables.append(I2)
            return True

        elif type_of_element == 'VCCS':
            node_A1 = element[2][0]
            node_A2 = element[2][1]
            node_B1 = element[3][0]
            node_B2 = element[3][1]
            transconductance = sympy.symbols(str(element[4])) #razmatranje
            self.node_currents[node_B1] += transconductance * (self.node_potentials[node_A1] - self.node_potentials[node_A2])
            self.node_currents[node_B2] -= transconductance * (self.node_potentials[node_A1] - self.node_potentials[node_A2])
            return True

        elif type_of_element == 'CCCS':
            node_A1 = element[2][0]
            node_A2 = element[2][1]
            node_B1 = element[3][0]
            node_B2 = element[3][1]
            amplification = sympy.symbols(str(element[4])) #razmatranje
            I1 = sympy.symbols('I' + element[1])
            self.node_currents[node_A1] += I1
            self.node_currents[node_A2] -= I1
            self.node_currents[node_B1] += amplification * I1
            self.node_currents[node_B2] -= amplification * I1
            self.voltage_equations.append(self.node_potentials[node_A1] - self.node_potentials[node_A2])
            self.current_variables.append(I1)
            return True

        elif type_of_element == 'CCVS':
            node_A1 = element[2][0]
            node_A2 = element[2][1]
            node_B1 = element[3][0]
            node_B2 = element[3][1]
            transresistance = sympy.symbols(str(element[4])) #razmatranje
            I2 = sympy.symbols('I' + element[1])
            self.node_currents[node_A1] += (self.node_potentials[node_B1] - self.node_potentials[node_B2])/transresistance
            self.node_currents[node_A2] -= (self.node_potentials[node_B1] - self.node_potentials[node_B2])/transresistance
            self.node_currents[node_B1] += I2
            self.node_currents[node_B2] -= I2
            self.voltage_equations.append(self.node_potentials[node_A1] - self.node_potentials[node_A2])
            self.current_variables.append(I2)
            return True

        elif type_of_element == 'L':
            node_A = element[2]
            node_B = element[3]
            I0 = 0
            if len(element) == 5:
                I0 = sympy.Symbol(element[4])

            if self.time_domain == True:
                 I0 = 0
            L = sympy.symbols(element[1])
            self.node_currents[node_A] += (self.node_potentials[node_A] - self.node_potentials[node_B]) / (self.s * L) + I0 / self.s
            self.node_currents[node_B] += (self.node_potentials[node_B] - self.node_potentials[node_A]) / (self.s * L) - I0 / self.s
            return True
            
        elif type_of_element == 'C':
            node_A = element[2]
            node_B = element[3]
            U0 = 0
            if len(element) == 5:
                U0 = sympy.Symbol(element[4])

            if self.time_domain == True:
                 U0 = 0
            C = sympy.symbols(element[1])
            self.node_currents[node_A] += (self.node_potentials[node_A] - self.node_potentials[node_B]) * self.s * C - U0 * C
            self.node_currents[node_B] += (self.node_potentials[node_B] - self.node_potentials[node_A]) * self.s * C + U0 * C
            
            return True
        
        
        #elif dodoati i ostale elemente koji ne zahtevaju diferencijalne jednacine        

        else:
            return False
        
    def __reinitialization(self):        
        self.voltage_equations = [] # JJ
        self.current_variables = [] # VV
        self.time_domain = False

    def symPyCAP(self, omega = "", spec_list = []):
    
        #------------- Empty all reused lists ------------------
        self.__reinitialization()

        #------------- Time (in)variant analysis ---------------
        if omega == "":
            self.time_domain = True
            self.s = sympy.symbol('s')
        else:
            w = sympy.Symbol(omega)
            self.time_domain = False
            self.s = sympy.Symbol('j' + str(w))
        
        #------------ Init of J = {0} and V to symbols Vi ----------------------
        self.__node_currents_init()
        self.__potential_symbols_definition() # define Vi potentials 
        
        #-------------- Init of user defined symbols -----------------------
        # Ovde lista simbola dolazi do izrazaja! i sve svoje mociiiiiiii bum
        for element in self.element_list:
            self.element_symbols[element[1]] = sympy.symbols(element[1])

        #------------- For every element in circuit, creating MNA equations -------
        result = list(map(self.__make_MNA_equation, self.element_list))

        #------------- Check validity of every element: TRY-CATCH-FINALLY -------
        for validation in result:
            if not validation:
                print("Unknown element:",self.element_list[result.index(validation)][0])
                return[]
                
        #------------- Solving linear system of equations by variables -------
        self.equations = self.node_currents[1:self.number_of_nodes]
        self.equations.extend(self.voltage_equations)    
        
        self.variables = self.node_potentials[1:self.number_of_nodes]
        self.variables.extend(self.current_variables)
        #self.electric_circuit_specifications()

        solution = sympy.linsolve(self.equations, self.variables)
        #print(solution)

        #------------- Preparing solution for output -------
        self.variables = [str(variable) for variable in self.variables]
        self.solution = dict(zip(self.variables, next(iter(solution)))) 

        return self.solution
    
    def electric_circuit_specifications(self):
        
        print("Circuit specifications: ")
        print("Number of nodes: " + str(self.number_of_nodes))
        print("Input elements:")
        for element in self.element_list:
            print(element)
        print("Equations: ", self.equations)
        print("Variables: ", self.variables)
        print()

    def output_solution(self):
        if self.solution == {}:
            print("Solution doesn't computed yet!")
        else:
            for sol in self.solution:
                print(sol,":",self.solution[str(sol)])