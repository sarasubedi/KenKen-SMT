#!/usr/bin/env python3
import sys
import re
import itertools

def print_header(variables, num_rows = 7, num_cols = 7):
    # same for every num_rows x num_cols kenken (defult is 7x7)
    print("(set-logic UFNIA)")
    print("(set-option :produce-models true)")
    print("(set-option :produce-assignments true)")
    # declare all of the variables in the kenken grid
    print("\n".join([f"(declare-const {n} Int)" for n in variables]))
    # bind all variables from 0-6
    print("\n".join([f"(assert (and (> {n} 0) (< {n} {num_cols})))" for n in variables]))
    # make sure each row has different values
    for i in range(num_rows):
        row = variables[i * num_cols: (i + 1) * num_cols]
        print(f"(assert (distinct {' '.join(row)}))")
    # make sure each column has different values
    for i in range(num_cols):
        row = variables[i::num_cols]
        print(f"(assert (distinct {' '.join(row)}))")

def print_footer(variables):
    print("(check-sat)")
    print(f"(get-value ({' '.join(variables)}))")
    print("(exit)")

def output_file(rule_dict, num_rows = 7, num_cols = 7):
    variables = [f"V{i}" for i in range(num_rows * num_cols)]
    # the header is the same for every kenken 
    # these will include basic rules
    print_header(variables)
    
    # this is what will be different based on the specific kenken
    for rule in rule_dict.values():
        value, operator, included_vars = rule
        temp = []
        for i in included_vars:
            temp.append(variables[i])
        if operator == '+' or operator == '*':
            print(f"(assert (= {value} ({operator} {' '.join(temp)})))")
        elif operator == '=':
            print(f"(assert (= {' '.join(temp)} {value}))")
        else: # division or subtraction
            print(f"(assert (or (= {value} ({operator} {' '.join(temp)}))(= {value} ({operator} {' '.join(temp[::-1])}))))")

    # footer of file
    print_footer(variables)
    

def kenken2smt():
    # Read in the input file, also removing whitespace, to get the sudoku puzzle 2D array
    input = sys.stdin.read().strip()
    # print(input)
    rule_pat = r"r\d+\.\d+[^,]?"
    rules = [match for line in input.split('\n') for match in re.findall(rule_pat, line)]
    grid_pat = r"r\d+"
    grid = [re.findall(grid_pat, line) for line in input.split('\n')[1:]]
    num_cols = len(grid)
    num_rows = len(grid[0])
    # for g in grid:
    #     print(g)
    # print(rules)
    rule_dict = {}
    for r in rules:
        temp = r.split('.')
        rule_name = temp[0]
        match = re.match(r'(\d+)([+*/-]?)', temp[1])
        num, op = match.groups()
        if op == '':
            op = '='
        rule_dict[rule_name] = (num, op, [])

    for n, line in enumerate(grid):
        for i in range(len(line)):
            rule_dict[line[i]][2].append(n*num_cols+i)

    print(rule_dict)
    output_file(rule_dict, num_rows, num_cols)

if __name__ == "__main__":
    kenken2smt()
