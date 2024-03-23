import json

def pretty_print_puzzle(json_data):
    puzzle_data = json.loads(json_data)['data']
    A, T, S, V, H = puzzle_data.split()

    # Convert strings into lists of lists
    A = [[int(num) for num in row.split()] for row in A.strip().split('\n')]
    T = [[int(num) for num in row.split()] for row in T.strip().split('\n')]
    S = [[sym if sym != '0' else '' for sym in row.split()] for row in S.strip().split('\n')]
    V = [[int(num) for num in row.split()] for row in V.strip().split('\n')]
    H = [[int(num) for num in row.split()] for row in H.strip().split('\n')]

    size = len(A)

    # Print the puzzle
    for i in range(size):
        if i % size != 0:
            print('-' * (size * 4 + size - 1))

        for j in range(size):
            if j % size != 0:
                print('|', end=' ')

            print(f'{A[i][j]:2}', end=' ')

            if H[j][i] == 1:
                print('-', end=' ')
        print()

        if i == size - 1:
            break

        for j in range(size):
            if j % size != 0:
                print('|', end=' ')

            print('   ' if T[i][j] == 0 else f' {S[i][j]} ', end=' ')

            if V[i][j] == 1:
                print('|', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage:
json_data = '''
{
  "data": "1 3 0 4 0\n0 2 0 0 0\n0 0 2 0 0\n0 0 0 0 0\n0 0 0 0 0\n\n0 0 0 0 0\n0 0 4 0 0\n0 0 0 0 0\n0 0 0 3 0\n0 0 0 0 0\n\n+ 0 + 0 +\n0 0 0 0 0\n+ 0 + 0 +\n0 0 0 0 0\n+ 0 + 0 +\n\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n"
}
'''

pretty_print_puzzle(json_data)
