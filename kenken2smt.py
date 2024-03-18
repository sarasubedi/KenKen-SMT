#!/usr/bin/env python3
import sys
import re

def output_file():
    print("(set-logic UFNIA)")
    print("(set-option :produce-models true)")
    print("(set-option :produce-assignments true)")
    for n in range(7*7):
        print("(declare-const V",n," Int)", sep='')
    for n in range(7*7):
        print("(assert (and (> V",n," 0) (< V",n," 10)))", sep='')



def kenken2smt():
    # Read in the input file, also removing whitespace, to get the sudoku puzzle 2D array
    input = sys.stdin.read().strip()
    # print(input)
    rule_pat = r"r\d+\.\d+[^,]?"
    rules = [match for line in input.split('\n') for match in re.findall(rule_pat, line)]
    grid_pat = r"r\d+"
    grid = [re.findall(grid_pat, line) for line in input.split('\n')[1:]]
    # for g in grid:
    #     print(g)
    # print(rules)
    rule_dict = {}
    for r in rules:
        temp = r.split('.')
        rule_dict[temp[0]] = temp[1]
    # print(rule_dict)
    # for rule,meaning in rule_dict.items():
    #     print(rule,meaning)
    output_file()

if __name__ == "__main__":
    kenken2smt()
