# KenKen Solver

## Group Information
**Group 13**
- Sara Subedi - V00986656
- Angus Bews - V00980317
- Julia Hoang - V00974641

## Background
In this project, we have developed a program to translate partially solved KenKen puzzles into SMT-LIB format. This format can be used with SMT solvers like MathSAT to generate solutions. The project consists of three main Python files: `kenken2smt.py`, `smt2kenken.py`, and `pp.py`.

## How to Use

### STEP 1. kenken2smt.py
This file contains functions to convert KenKen puzzles into SMT-LIB format. It includes functions to print the header and footer of the SMT-LIB file, as well as to generate the main content based on the given puzzle rules.

#### Usage:
```bash
python3 ./kenken2smt.py <puzzle.txt >puzzle.smt
```

NOTE: Please ensure the input `puzzle.txt` file is in the following format:
```
#kenken www.kenkenpuzzle.com Puzzle 21995 7x7 Easiest
r1.112*,r2.6-,r2,r3.90*,r3,r3,r4.12+
r1,r1,r5.8+,r5,r6.6,r7.48*,r4
r8.30*,r8,r5,r9.10+,r10.3+,r7,r4
r11.6+,r11,r12.3,r9,r10,r7,r13.3-
r14.3/,r15.12+,r16.140*,r16,r16,r17.3/,r13
r14,r15,r15,r18.80*,r18,r17,r19.18+
r20.18*,r20,r20,r21.2,r18,r19,r19
```

### STEP 2. smt2kenken.py
This file contains functions to convert SMT-LIB format solutions into KenKen puzzles. It includes functions to parse the SMT-LIB file and generate the corresponding KenKen puzzle.

#### Usage:
```bash
mathsat <puzzle.smt >model.smt
python3 ./smt2kenken.py <model.smt >solution.txt
cat solution.txt
```

### STEP 3. pp.py
This file contains functions to pretty print KenKen puzzles and solutions. It includes functions to print the KenKen puzzle and solution in a readable format.

#### Usage:
```bash
python3 ./pp.py
<puzzle ID>
```

Example:
```bash
python3 ./pp.py
21995
```

