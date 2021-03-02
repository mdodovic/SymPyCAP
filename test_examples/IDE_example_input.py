from symPyCAP import Circuit
import sympy

if __name__ == "__main__":

    circuit = [
        ["V","Vg",1,0],
        ["R","R1",1,2],
        ["R","R2",2,0]
    ]
    
    voltage_divider = Circuit(circuit)

    R = sympy.Symbol('R');
    
    voltage_divider.symPyCAP()
    voltage_divider.symPyCAP(r = {"R1" : R, "R2" : R})

    voltage_divider.print_solutions()

    voltage_divider.print_specific_solutions()
    
