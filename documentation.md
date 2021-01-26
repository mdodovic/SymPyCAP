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
(It's written entirely in Python) and uses SymPy, a Python library for symbolic mathematics.\
SymPyCAP uses MNA (Modified Nodal Analysis) to formulate and solve equations.

## Why SymPy?  

* SymPy is completely free, open source and licensed under the BSD license. So, you can modify the source code end sell it if you want to.

* SymPy uses Python as its language. This means that if you know Python, it is much easier to get started with SymPy (because you already knows the syntax). And if you don't know Python, it is really easy to learn. 

* Third advantage of SymPy is that it is lightweight program. It has no dependencies other than Python, so it can be used almost anywhere easily. 

* And finally, it can be used as a library. You can just import it in your own Python application.

## Algorithm 

#### Nodes:

* Reference node - one node, labeled by zero, 0 (default node). The node voltage of this node (reference node) is set to zero, 0.
* Other nodes - labeled by consecutive integers, starting from one, 1.

#### The Kirchhoff’s current law equations (KCL)

* SymPyCAP formulates the KCL equations for all nodes, except reference node (for *other nodes*).

#### Passive sign convention

![smer.png](C:\Users\jelana\Desktop\smer.png)
* Whenever the reference direction for the current in an element is in the direction of the reference voltage drop across the element (as in this picture), use a positive sign in any expression that relates the voltage to the current. Otherwise, use a negative sign.

* We apply this sign convention.


#### Modified Nodal Analysis

<ins> *MNA variables:* </ins> node voltages and currents which cannot be expressed in terms of node voltages.
* Node voltages are labeled by V1, V2, V3...
* V0 = 0, by default
* Currents are labeled by I"id" ("id" specifies a circuit element).


#### Reserved symbols

* *I* - MNA current variables ( I[id] )
* *V* - MNA voltage variables (V0, V1, V2...)
* *r* - dictionary of replacements in the form:\
{..., "id" : symbolic_value, ...}
* *replacement* - another name for r
* *w* - symbol/symbolic expression of frequency for time-invariant analysis
* *omega* - another name for w



## Electric Circuit  

Input to SymPyCAP (the circuit to be analyzed) is specified as a list of circuit elements (list
 of lists):
 
   `[list_1, list_2, list_3, ... list_N]`

A circuit element (list_i) is specified as a list:

* for one-port element:\
     `[type, id, a, b]`\
     `[type, id, a, b, IC]`
           
* for two-port element:\
     `[type, id, [a1,a2], [b1,b2], p]`\
     `[type, id, [a1,a2], b]`\
     (b = b1 when b2 is ground node)
                        

*type* - string that specifies type of element ("R", "L", "C", "Z", "Y", "I", "V", "OpAmp", "IdealT", "InductiveT", "VCVS", "VCCS", "CCCS", "CCVS")\
*id* - string that identifies circuit element ("R1", "L1", "C1", "Ug", "OpAmp1", "I1", "VCVS1", etc.)\
*a* - positive terminal\
*b* - negative terminal\
*IC* - initial conditions at t_[0]- (V0 for capacitors, I0 for inductors,  [I_01,I_02] for linear inductive transformers)\
*a1* - positive terminal of the 1st port\
*a2* - negative terminal of the 1st port\
*b1* - positive terminal of the 2nd port\
*b2* - negative terminal of the 2nd port\
*p* - parameter of parameters
 
#### One-port elements: 

* <ins> **Resistor** </ins>\
     `["R", "id", plusTerm, minusTerm]`
     
* <ins> **Capacitor** </ins>\
     `["C", "id", plusTerm, minusTerm, "U0"]`\
     `["C", "id", plusTerm, minusTerm]`\
     U0 is here 0, by default.

* <ins> **Inductor** </ins>\
     `["L", "id", plusTerm, minusTerm, "I0"]`\
     `["L", "id", plusTerm, minusTerm]`\
    I0 is here 0, by default.
     
* <ins> **Impedance** </ins>\
     `["Z", "id", plusTerm, minusTerm]`

* <ins> **Admitance** </ins>\
     `["Y", "id", plusTerm, minusTerm]`

* <ins> **Current source - ideal current generator** </ins>\
     `["I", "id", plusTerm, minusTerm]`
         

* <ins> **Voltage source - ideal voltage generator** </ins>\
     `["V", "id", plusTerm, minusTerm]`
      ( V = V [plusTerm] - V [minusTerm] )

#### Two-port elements: 

* <ins> **Operational Amplifier - Ideal OpAmp** </ins>\
     `["OpAmp", "id", [nonInvertingTerm, invertingTerm], 2ndTerm]`
* <ins> **ABCD two-port** </ins>\
     `["ABCD", "id", [plusPrimaryTerm, minusPrimaryTerm], [plusSecondaryTerm, minusSecondaryTerm], [["A", "B", "C", "D"]]]`

#### Controlled Sources: 

* <ins> **VCVS - Voltage Controlled Voltage Source** </ins>\
     `["VCVS", "id", [plusControllingTerm, minusControllingTerm], [plusControlledTerm, minusControlledTerm], "voltageGain"]`
     
    

* <ins> **VCCS - Voltage Controlled Current Source** </ins>\
    `["VCCS", "id", [plusControllingTerm, minusControllingTerm], [plusControlledTerm, minusControlledTerm], "transconductance"]`

* <ins> **CCCS - Current Controlled Current Source** </ins>\
     `["CCCS", "id", [plusControllingTerm, minusControllingTerm], [plusControlledTerm,  minusControlledTerm], "currentGain"]`
    

* <ins> **CCVS - Current Controlled Voltage Source** </ins>\
     `["CCVS", "id", [plusControllingTerm, minusControllingTerm], [plusControlledTerm, minusControlledTerm], "transresistance"]`
     
#### Transformers:

* <ins> **Ideal Transformer** </ins>\
     `["IdealT", "id", [plusPrimaryTerm, minusPrimaryTerm], [plusSecondaryTerm, minusSecondaryTerm], turnsRatio]`

* <ins> **Inductive Transformer** </ins>\
`["InductiveT", "id", [plusPrimaryTerminal, minusPrimaryTerminal], [plusSecondaryTerminal, minusSecondaryTerminal], [L1,L2,L12]]`

    `["InductiveT", "id", [plusPrimaryTerminal, minusPrimaryTerminal], [plusSecondaryTerminal, minusSecondaryTerminal], [L1,L2,L12], [I_01,I_02]]`


## Calling SymPyCAP  

* <ins> **Importing symbols:** </ins>

`from symPyCAP_oop import Solution
from sympy import symbols
S1, S2,.. = symbols('S1,S2')
`

-symbols() function returns a sequence of symbols with names taken from names argument, which can be a comma or whitespace delimited string, or a sequence of strings\
-*S1,S2* - symbols that will be used for circuit analysis (for example: E, R, L, W..). In this sequence can't be reserved symbols.

* <ins> **For time-invariant analysis:** </ins>

`from symPyCAP_oop import Solution
from sympy import symbols
system = Solution(elements)
solution = system.symPyCAP()
`

-*elements* - arbitrary name for list of circuit elements (it can be any other word..)\
-*system* - instance of class Solution (main class of the program)\
-`symPyCAP()` - this method initializes V (to Vi), user defined symbols, creates MNA equations, for every element in circuit, solves linear system of equations by variables, checks validity of every element and returns the solution\
-also, it can read replacement list for user symbols,  for example:\
 -> `solution = system.symPyCAP(replacement = {"R1" : R, "R2" : R})`\
 -> `solution = system.symPyCAP(r = {"R1" : R, "R2" : R})`
 
* <ins> **For time varying excitations:** </ins>

`
from symPyCAP_oop import Solution
from sympy import symbols
system = Solution(elements)
solution = system.symPyCAP("W")
`

*W* - angular frequency [rad/s]

<ins>It can be replaced with:</ins>\
  -> "  "  `solution = system.symPyCAP()`\
  this means that frequency is not specified - by default, it will be marked as "s" in the solution\
  -> w = "W"   `solution = system.symPyCAP( w = "W")`\
  -> omega = "W"  `solution = system.symPyCAP( omega = "W")`\
-in this version, also, method can read replacement list, for example:\
 `solution = system.symPyCAP( w= "W", replacement = {"R1" : R, "R2" : R})` etc.

* <ins> **Outputs** </ins>

**1)** `print(solution)` - this function returns the solution in the following form:\
*{ variable1: solution(variable1), variable2: solution(variable2)... }*

**2)** 
`
for sol in solution:`
           `print(sol,":",solution[str(sol)])
`
           
   -solution in form:\
           *variable1: solution(variable1)*\
           *variable2: solution(variable2)*\
           ...

**3)** `print(solution['Vi']) ` - solution for a single node (Vi):\
*solution(Vi)*

**4)** 

`from symPyCAP_oop import Solution`\
`from sympy import symbols`\
`system = Solution(elements)`\
`solution = system.symPyCAP()`

`system.electric_circuit_specifications()` - this function returns:

*Circuit specifications:  *\
Number of nodes: <"positive_integer">\
Input elements: <"list of elements">*\
*Replacement rule:  { <"element_values"> }*\
*Equations:  [ I["id"]=... ]*\
Variables:  [ V1, ... Vn, I["id"]...]*

**5)** `system.print_solutions()` - returns exactly like 2):\
*variable1: solution(variable1)*\
*variable2: solution(variable2)*\
...

**6)** `system.print_specific_solutions()` - - returns the solution in the same form as 5) and 2), <ins> but with applied replacement rules ("R1" : R, "C2" : C,...) </ins>\
-Replacement rule physically changes id with symbols, so this function can return the solution in the form 1/0.


* <ins> **Getters** </ins>

**1)** `get_solutions()`
        
    
**2)** `get_specific_solutions()`
        

 

## References


Allen Downey, Think Python: How to Think Like a Computer Scientist, Green
Tea Press, 2008.

Paul Gerrard, Lean Python: Learn Just Enough Python to Build Useful Tools,
Apress, 2016.



##### Classic

Charles A. Desoer, Ernest S. Kuh,
Basic Circuit Theory, New York, NY, McGraw-Hill, 1969.

Leon O. Chua, Charles A. Desoer, and Ernest S. Kuh,
Linear and nonlinear circuits, New York, NY, McGraw-Hill, 1987.



##### General

Charles K. Alexander, Matthew N. O. Sadiku,
Fundamentals of Electric Circuits, 6/e, New York, NY, McGraw-Hill, 2017.

James W. Nilsson, Susan A. Riedel,
Electric Circuits, 10/e, Upper Saddle River, NJ, Prentice Hall, 2015.

J. David Irwin, R. Mark Nelms,
Basic Engineering Circuit Analysis, 11/e, Hoboken, NJ, Wiley, 2015.

James A. Svoboda, Richard C. Dorf,
Introduction to Electric Circuits, 9/e, Hoboken, NJ, Wiley, 2014.

William H. Hayt, Jr., Jack E. Kemmerly, Steven M. Durbin,
Engineering circuit analysis, 8/e, New York, NY, McGraw-Hill, 2012.

Farid N. Najm, Circuit Simulation,
Hoboken, New Jersey, John Wiley & Sons, 2010.

Omar Wing, Classical Circuit Theory,
Springer Science+Business Media, LLC, New York, NY, 2008.

Wai-Kai Chen (Editor),
Circuit Analysis and Feedback Amplifier Theory,
CRC Press, Taylor & Francis Group, Boca Raton, FL, 2006.



##### Power Engineering

Arieh L. Shenkman, Transient Analysis of Electric Power Circuits Handbook,
Springer,  Dordrecht, The Netherlands, 2005.

Arieh L. Shenkman, Circuit Analysis for Power Engineering Handbook,
Springer, Dordrecht, The Netherlands, 1998.



##### Transmission Lines

Paul R. Clayton, Analysis of Multiconductor Transmission Lines, 2/e,
Hoboken, NJ, Wiley IEEE Press, 2008.



