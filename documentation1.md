# <ins>Documentation for SymPyCAP</ins>



##  Author  

* Katarina Stanković
* Nikola Ilić
* Matija Dodović
* Jelena Bakić
* Prof. Dr Dejan V. Tošić
* Prof. Dr Milka M. Potrebić

University of Belgrade - School of Electrical Engineering

## License  

Creative Commons

## Acknowledgment 

We thank Prof. Dr Dejan V. Tošić for recommending this software project to us and for all discussions and help with the project.

## About SymPyCAP 

SymPyCAP is program for solving linear, time-invariant electric circuits. This program is Python-based 
(It's written entirely in Python) and uses SymPy, a Python library for symbolic mathematics.

## Why SymPy?  

* SymPy is completely free, open source and licensed under the BSD license. So, you can modify the 
source code end sell it if you want to.
* SymPy uses Python as its language. This means that if you
know Python, it is much easier to get started with SymPy (because you already knows the syntax). 
And if you don't know Python, it is really easy to learn. 
* Third advantage of SymPy is that it is lightweight program. It has no dependencies other than Python,
so it can be used almost anywhere easily. 
* And finally, it can be used as a library. You can just import it in your own Python application.

## Algorithm 

#### Nodes:

* Reference node - one node, labeled by zero, 0 (default node). The node voltage of this node (reference node) is set to zero, 0.
* Other nodes - labeled by consecutive integers, starting from one, 1.

#### The Kirchhoff’s current law equations

* SymPyCAP formulates the KCL equations for all nodes, except reference node (for *other nodes*).
* The currents are expressed in terms of node voltages.
* The reference direction for current is **out of the node**.

#### Modified Nodal Analysis

SymPyCAP uses MNA (Modified Nodal Analysis) to formulate ande solve equations.\
<ins> *MNA variables:* </ins> node voltages and currents which cannot be expressed in terms of node voltages.\
* Node voltages are labeled by V1, V2, V3...
* V0 = 0 by default
* Currents are labeled by I"ID" ("ID" specifies a circuit element).

##   Units   
 
All quantities are in the International System of Units (SI).

## Electric Circuit  

The input of this program (the circuit to be analyzed) is specified as a list of circuit elements (list
 of lists):
 
   `[list_1, list_2, list_3, ... list_N]`

A circuit element (list_I) is specified as a list:

* for one-port element:\
           `[type, label, a, b] `\
           `[type, label, a, b, IC]`\
* for two-port element:\
     `[type, label, [a1,a2], [b1,b2], p]`\
     `[type, label, [a1,a2], b]*` (b = b1 when b2 is ground node)
                        

*type* - string that specifies type of element ("R", "L", "C", "Z", "Y", "I", "V", "OpAmp", "IdelalT", "InductiveT", "VCVS", "VCCS", "CCCS", "CCVS")\
*label* - string that identifies circuit element ("R1", "L1", "C1", "Ug", "OpAmp1", "I1", "VCVS1", etc.)\
*a* - positive terminal\
*b* - negative terminal\
*IC* - initial conditions at 0 - minus\
*a1* - positive terminal of the 1st port\
*a2* - negative terminal of the 1st port\
*b1* - positive terminal of the 2nd port\
*b2* - negative terminal of the 2nd port\
*p* - parameter of parameters
 
#### One-port elements: 

* <ins> **Resistor** </ins>\
     `["R", "ID", plusTerm, minusTerm]`
     
* <ins> **Capacitor** </ins>\
     `["C", "ID", plusTermi, minusTerm, "U0"]`\
     -U0 is initial condition, initial voltage at 0 - minus ( U0 = V [plusTerm] - V [minusTerm] )\
     `["C", "ID", plusTermi, minusTerm]`\
     U0 is here 0, by default (for time domain)

* <ins> **Inductor** </ins>\
     `["L", "ID", plusTerm, minusTerm, "I0"]`\
     -I0 is initial condition, initial current at 0 - minus (from plusTerm, across the element, to minusTerm)\
     `["L", "ID", plusTerm, minusTerm]`\
     -I0 is here 0, by default (for time domain)
     
* <ins> **Impedance** </ins>\
     `["Z", "ID", plusTerm, minusTerm]`

* <ins> **Admitance** </ins>\
     `["Y", "ID", plusTerm, minusTerm]`

* <ins> **Current source - ideal current generator** </ins>\
     `["I", "ID", plusTerm, minusTerm]`\
      (from plusTerm, across the element, to minusTerm)     

* <ins> **Voltage source - ideal voltage generator** </ins>\
     `["V", "ID", plusTerm, minusTerm]`\
      ( V = V [plusTerm] - V [minusTerm] )

#### Two-port elements: 

* <ins> **Operational Amplifier - Ideal OpAmp** </ins>\
     `["OpAmp", "ID", [nonInvertingTerm, invertingTerm], 2ndTerm]`
* <ins> **ABCD two-port** </ins>\
     `["ABCD", "ID", [plusPrimaryTerm minusPrimaryTerm], [plusSecondaryTerm, minusSecondaryTerm], [["A", "B", "C", "D"]]]`

#### Controlled Sources: 

* <ins> **VCVS** </ins>\
     `["VCVS","ID",[plusControllingTerm, minusControllingTerm],[plusControlledTerm, minusControlledTerm], "voltageGain"]`\
     -I["ID"] is current into plusControlledTerm

* <ins> **VCCS** </ins>\
    `["VCCS","ID",[plusControllingTerm, minusControllingTerm],[plusControlledTerm, minusControlledTerm], "transconductance"]`

* <ins> **CCCS** </ins>\
     `["CCCS","ID",[plusControllingTerm, minusControllingTerm],[plusControlledTerm, minusControlledTerm],"currentGain"]`\
     -I["ID"] is current into plusControllingTerm

* <ins> **CCVS** </ins>\
     `["CCVS","ID",[plusControllingTerm, minusControllingTerm],[plusControlledTerm, minusControlledTerm],"transresistance"]`
     
#### Transformers:

* <ins> **Ideal Transformer** </ins>\
     `["IT", "id", [plusPrimaryTerm, minusPrimaryTerm], [plusSecondaryTerm, minusSecondaryTerm], turnsRatio]`

* <ins> **Inductive Transformer** </ins>\
     `["K", "id", [plusPrimaryTerminal, minusPrimaryTerminal], [plusSecondaryTerminal, minusSecondaryTerminal], [L1,L2,L12], [Io1,Io2]]`


## Calling SymPyCAP  

* <ins> **For time-invariant analysis:** </ins>
```
system = Solution(elements)
solution = system.symPyCAP()
```
-*elements* - arbitrary name for list of circuit elements (it can be any other word..)\
-*system* - instance of class Solution (main class of the program)\
-`symPyCAP()` - this method initializes V (to Vi), user defined symbols, creates MNA equations, for every element in circuit, solves linear system of equations by variables, checks validity of every element and returns the solution\
-also, it can read replacement list for user symbols,  for example:\
 -> `solution = system.symPyCAP(replacement = ["R1=R", "R2=R"])`\
 -> `solution = system.symPyCAP(r = ["R1=R", "R2=R"])`\
 
 * <ins> **For time-variant analysis:** </ins>
```
system = Solution(elements)
solution = system.symPyCAP("W")
```
-*"W"* - complex frequency.\
It can be replaced with:\
  -> " "  `solution = system.symPyCAP()`\ 
  this means that frequency is not specified - by default, it will be marked as "s" in the solution\
  -> w = "W"   `solution = system.symPyCAP( w = "W")`\
  -> omega = "W"  `solution = system.symPyCAP( omega = "W")`\
-in this version, also, method can read replacement list, for example:\
- `solution = system.symPyCAP( w= "W", replacement = ["R1=R", "R2=R"])` etc.

* <ins> **Outputs** </ins>

**1)** `print(solution)` - this function returns the solution in the following form:\
*{ variable1: solution(variable1), variable2: solution(variable2)... }*

**2)**
```
       for sol in solution:
           print(sol,":",solution[str(sol)])
```     
          
   -solution in form: variable1: solution(variable1)\
                      variable2: solution(variable2)\
                      ...

**3)**

....
