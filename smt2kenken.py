#!/usr/bin/env python3
import sys
import re

def smt2kenken():
    # Read in the input file, also removing whitespace, to get the sudoku puzzle 2D array
    input = sys.stdin.read().split('\n')
    
    solution = ""
    
    if("unsat" == input[0]):
        print("Problem is unsatisfiable.")
    
    for line in input:
        match = re.search(r"\(V\d+ (\d+)\)", line)
        if match:
            solution += match.group(1)
    
    print(solution)
    
if __name__ == "__main__":
    smt2kenken()