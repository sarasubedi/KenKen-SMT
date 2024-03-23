#!/usr/bin/env python3

import os
import re

dat_patt = re.compile(r",\"data\":\"(.*)\",\"size")

def pretty_print_puzzle(json_data):
    #print(json_data)
    A, T, S, V, H = re.split('A|T|S|V|H', json_data)[1:] #drop the initial blank

    # Convert strings into lists of lists
    A = [[int(num) for num in row.split()] for row in A.strip().split('\n')]
    T = [[int(num) for num in row.split()] for row in T.strip().split('\n')]
    S = [[sym for sym in row.split()] for row in S.strip().split('\n')]
    V = [[int(num) for num in row.split()] for row in V.strip().split('\n')]
    H = [[int(num) for num in row.split()] for row in H.strip().split('\n')]


    size = len(A)

    # Print the puzzle
    # Print horizontal lines for the top row
    print("+" + "-----+" * size)
    for row in range(size):
        underline = "+"
        print("|", end="")
        
        #Print out constraints for the row
        for column in range(size):
            if T[row][column] != 0:
                print(T[row][column], end="")
                if S[row][column] != str(1):
                    print(S[row][column], end="")
                else:
                    print(" ", end="")

                print(" " * (4-len(str(T[row][column]))), end="")
            else:
                print("     ",end="")

            if column == size-1 or V[row][column] == 1:
                print("|", end="")
            else:
                print(" ", end="")

        print("\n|", end="")
        
        
        #Print out numbers in that row
        for column in range(size):
            print(" ", A[row][column], end="  ")

            if column == size-1 or V[row][column] == 1:
                print("|", end="")
            else:
                print(" ", end="")

            if row == size-1 or H[column][row] == 1:
                underline += "-----+"
            else:
                underline += "     +"

        print("\n"+ underline)



if __name__ == "__main__":
    puz_id = input("Enter PuzzleID: ")
    json_data = os.popen(f"./fetch.sh {puz_id}").read()
    
    dat = dat_patt.search(json_data)
    if dat:
        pretty_print_puzzle(dat.group(1).replace("\\r\\n", "\n"))