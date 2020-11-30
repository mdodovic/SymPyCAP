# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@authors: 
    Katarina Stanković (sk180183d@student.etf.bg.ac.rs)
    Matija Dodović (dm180072d@student.etf.bg.ac.rs)
"""
from symPyCAP_oop import Solution

#elements = [ 
#            ["R", "R1", 2, 1],
#            ["R", "R2", 1, 0],
#            ["R", "R3", 1, 0],
#            ["V", "Ug", 2, 0] 
#            ]
#system = Solution(elements)
#solution = system.symPyCAP()
#for sol in solution:
#    print(sol,":",solution[str(sol)])

"""
solution = system.symPyCAP([]) # Treba se odluciti
print(solution) # celokupno resenje u formi var: resenje(var), ...
print(solution['V1']) # pojedinacan pristup resenjima
print(solution['V2'])
print(solution['IUg'])
"""

#Riordan_shema = [
#    ["V", "Ug", 1, 0],
#    ["OpAmp", "OpAmp1", [1,4], 5],
#    ["R", "R1", 4, 0],
#    ["R", "R2", 4, 5],
#    ["R", "R3", 5, 2],
#    ["OpAmp", "OpAmp2", [1,2], 3],
#    ["R", "R4", 2, 3],
#    ["R", "R5", 1, 3]
#]
#
#system = Solution(Riordan_shema)
#solution = system.symPyCAP()
#solution = system.symPyCAP()
#for sol in solution:
#    print(sol,":",solution[str(sol)])

#Sabirac = [
#    ["V", "E1", 1, 0],
#    ["V", "E2", 2, 0],
#    ["V", "E3", 3, 0],
#    ["R", "R", 1, 5],
#    ["R", "R", 2, 5],
#    ["R", "R", 3, 5],
#    ["R", "R", 5, 4],
#    ["OpAmp", "OpAmp1", [0, 5], 4]
#];
#system = Solution(Sabirac)
#solution = system.symPyCAP()
#for sol in solution:
#    print(sol,":",solution[str(sol)])

#elements = [
#["V","E1",7,6],
#["R","R",7,8],
#["R","R",6,3],
#["R","R",7,4],
#["I","I1",8,5],
#["I","I2",4,3],
#["R","R",5,4],
#["R","R",3,1],
#["V","E2",0,4],
#["V","E3",2,5],
#["R","R",1,0],
#["R","R",2,0]
#]
#system = Solution(elements)
#solution = system.symPyCAP()
#for sol in solution:
#    print(sol,":",solution[str(sol)])
    
    
#elements = [
#    ["VCVS", "VCVS1",[2,0],[3,0],5],
#    ["V","E1",1,0],
#    ["R","R1",1,2],
#    ["R","R2",2,0],
#    ["R","R3",3,0],
#    ["R","R4",3,0]
#]

#elements = [
#    ["CCVS","CCVS1",[2,0],[3,0],"r1"],
#    ["VCCS","VCCS1",[3,0],[4,0],"g1"],
#    ["I","I1",1,0],
#    ["R","R1",2,1],
#    ["R","R2",2,0],
#    ["R","R3",4,0]
#]

#elements = [
#    ["VCVS","VCVS1",[2,0],[3,0],"a1"],
#    ["VCCS","VCCS1",[3,0],[4,0],"g1"],
#    ["CCCS","CCCS1",[4,0],[5,0],"a2"],
#    ["CCVS","CCVS1",[5,0],[6,0],"r1"],
#    ["V","E1",1,0],
#    ["R","R1",1,2],
#    ["R","R2",2,0],
#    ["R","R3",6,7],
#    ["R","R4",7,0]
#]
#
#
#system = Solution(elements)
#solution = system.symPyCAP()
#system.electric_circuit_specifications()
#print(solution)
#for key, value in solution.items():
#    print(key, ":", value)
#
#print(solution['V2'])


#elements = [
#    ["V","E1",1,0],
#    ["R","R1",1,2],
#    ["R","R2",2,0],
#]
#
#system = Solution(elements)
#
#solution = system.symPyCAP(replacement = ["R1=R", "R2=R"])
#
##system.electric_circuit_specifications()
#system.print_solutions()
#system.print_specific_solutions()
#system.print_solutions()

#------------------- Dinamicki elementi ---------------------------------------

#LC_circuit = [
#    ["L","L1",2,0],
#    ["C","C1",1,0],
#    ["V","E1",1,0],
#    ["I","I1",2,1]
#    ]
#
#circuit = Solution(LC_circuit)
#
#solution = circuit.symPyCAP("W")
#
#circuit.electric_circuit_specifications()
#circuit.output_solution()


#OTA_C = [
#    ["V","E1",1,0],
#    ["R","R1",1,2],
#    ["C","C1",3,0],
#    ["VCCS","VCCS1",[0,2],[3,0],"g"],
#    ["VCCS","VCCS2",[3,0],[2,0],"g"]
#]
#circuit = Solution(OTA_C)
#
#solution = circuit.symPyCAP()
#
#circuit.electric_circuit_specifications()
#circuit.output_solution()


#LC_filter_sema = [
#    ["V","E",1,0],
#    ["R","R1",1,2],
#    ["C","C",2,3],
#    ["R","R2",3,0],
#    ["L","L",3,0]
#];
#values = ["R1=R", "R2 = R"]
#circuit = Solution(LC_filter_sema)
#
#solution = circuit.symPyCAP(w = "W", replacement = values)
#
#circuit.electric_circuit_specifications()
#circuit.output_solution()


#InductiveT = [
#    ["V","E1",1,0],
#    ["R","R1",1,2],
#    ["R","R2",2,3],
#    ["InductiveT","K1",[2,0],[3,0],["L1","L2","L12"],["I01",0]]
#    ]
#circuit = Solution(InductiveT)
#
#solution = circuit.symPyCAP()
#
#circuit.electric_circuit_specifications()
#circuit.output_solution()


RLC = [
    ["V","E1",1,0],
    ["R","R1",1,2],
    ["L","L1",2,3],
    ["C","C1",3,0,"U0"]
]

circuit = Solution(RLC)

solution = circuit.symPyCAP(omega = "W", r = ["E1=E", "R1=R", "C1=C","L1=L"])

circuit.electric_circuit_specifications()
#circuit.print_solutions()
circuit.print_specific_solutions()

#Initial_enegy = [
#    ["VCVS","VCVS1",[1,0],[3,0],"a"],
#    ["C","C1",1,0,"U0"],
#    ["R","R1",1,0],
#    ["R","R2",1,2],
#    ["C","C2",2,3],
#    ["R","R3",3,0]
#]
#
#
#
#circuit = Solution(Initial_enegy)
#
#solution = circuit.symPyCAP(replacement = ["C1=C", "R1=R", "R2=R", "C2=C","R3=R"])
#
#circuit.electric_circuit_specifications()
##circuit.print_solutions()
#circuit.print_specific_solutions()


#IT_circuit = [
#    ["IdealT","IT1",[1,0],[2,0],"n"],
#    ["V","E1",1,0],
#    ["R","R1",2,0]
#]
#circuit = Solution(IT_circuit)
#
#solution = circuit.symPyCAP(replacement = ["R1=R","E1=E"])
#
#circuit.electric_circuit_specifications()
##circuit.print_solutions()
#circuit.print_specific_solutions()

#quatropol = [
#    ["4-A","4-A1",[1,0],[2,0],["a","c","b","d"]],
#    ["V","E1",1,0],
#    ["R","R1",2,0]
#]
#circuit = Solution(quatropol)
#circuit.electric_circuit_specifications()
#solution = circuit.symPyCAP(replacement = ["R1=R","E1=E"])
#
#
##circuit.print_solutions()
#circuit.print_specific_solutions()

