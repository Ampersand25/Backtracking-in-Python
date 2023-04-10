def consistent(mat, line, col):
    for elem in range(9):
        if (elem != col and mat[line][col] == mat[line][elem]) or (elem != line and mat[line][col] == mat[elem][col]):
            return False
    ll, cc = (line // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if (ll + i != line or cc + j != col) and mat[ll + i][cc + j] == mat[line][col]:
                return False
    return True

def solution(line, col):
    return line + 1 == 9 and col + 1 == 9

def solutionFound(mat):
    with open('sudoku.out', 'w') as f:
        for line in range(9):
            for col in range(9):
                f.write(str(mat[line][col]))
                f.write(' ') if col != 8 else f.write('\n')
    exit(0)

def back(mat):
    for line in range(9):
        for col in range(9):
            if mat[line][col]:
                continue
            for k in range(1, 10):
                mat[line][col] = k
                if consistent(mat, line, col):
                    back(mat)
                mat[line][col] = 0
            return
    solutionFound(mat)

mat = [[None for i in range(9)] for j in range(9)]
with open('sudoku.in', 'r') as f:
    for l in range(9):
        line, idx = f.readline(), 0
        for c in range(9):
            mat[l][c] = int(line[idx])
            idx += 2
back(mat)