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

SymPyCAP uses MNA (Modified Nodal Analysis) to formulate 
equations.


##   Units   
 
All quantities are in the International System of Units (SI).

## Electric Circuit  

The input of this program (the circuit to be analyzed) is specified as a list of circuit elements (list
 of lists):
 
   `[list_1, list_2, list_3, ... list_N]`

A circuit element (list_I) is specified as a list:

* for one-port element:\
           `[type, label, a, b] `
     
* for two-port element:\
     `[type, label, [a1,a2], [b1,b2], p]`\
     `[type, label, [a1,a2], b]*` (b = b1 when b2 is ground node)
                        

*type* - string that specifies type of element ("R", "L", "C", "Z", "Y", "I", "V", "OpAmp", "IdelalT", "InductiveT", "VCVS", "VCCS", "CCCS", "CCVS")\
*label* - string that identifies circuit element ("R1", "L1", "C1", "Ug", "OpAmp1", "I1", "VCVS1", etc.)\
*a* - positive terminal\
*b* - negative terminal\
*a1* - positive terminal of the 1st port\
*a2* - negative terminal of the 1st port\
*b1* - positive terminal of the 2nd port\
*b2* - negative terminal of the 2nd port\
 
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
```
system = Solution(elements)
solution = system.symPyCAP()
```
....
