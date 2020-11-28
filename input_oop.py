# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:25:17 2020

@author: Katarina
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
#solution = system.symPyCAP()
#
#system.electric_circuit_specifications()
#system.output_solution()

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
#    ["R","R",1,2],
#    ["C","C",2,3],
#    ["R","R",3,0],
#    ["L","L",3,0]
#];
#circuit = Solution(LC_filter_sema)
#
#solution = circuit.symPyCAP("W")
#
#circuit.electric_circuit_specifications()
#circuit.output_solution()


InductiveT = [
    ["V","E1",1,0],
    ["R","R1",1,2],
    ["R","R2",2,3],
    ["InductiveT","LT1",[2,0],[3,0],["L1","L2","L12"],["I01","0"]]
    ]
circuit = Solution(InductiveT)

solution = circuit.symPyCAP()

circuit.electric_circuit_specifications()
circuit.output_solution()