nr_sol = 0

def consistent(mat, line, col):
    return True if line != col else not mat[line][col]

    '''
    if line == col:
        return not mat[line][col]
    return True
    '''

def solution(n, line, col):
    return line + 1 == n and col + 1 == n

def solutionFound(mat, n):
    global nr_sol
    nr_sol += 1
    print('\nGraful #' + str(nr_sol) + ': ')
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = ' ')
        print()

def recursive_backtr(mat, n, line = 0, col = 0):
    for comp in range(2):
        mat[line][col] = mat[col][line] = comp
        if consistent(mat, line, col):
            if solution(n, line, col):
                solutionFound(mat, n)
            else:
                if col + 1 == n:
                    recursive_backtr(mat, n, line + 1, line + 1)
                else:
                    recursive_backtr(mat, n, line, col + 1)

def main():
    n = int(input('n = '))
    mat = []
    for idx in range(n):
        line = [0] * n
        mat.append(line)
    recursive_backtr(mat, n)
    global nr_sol
    assert nr_sol == 2 ** (n * (n - 1) // 2)

main()