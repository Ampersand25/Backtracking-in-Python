nr_sol = 0

def consistent(mat, line, col):
    return not mat[line][col] if line == col else True

def solution(n, line, col):
    return line + 1 == n and col + 1 == n

def solutionFound(mat, n):
    global nr_sol
    nr_sol += 1
    print('\nGraful #' + str(nr_sol) + ': ')
    for l in range(n):
        for elem in mat[l]:
            print(elem, end = ' ')
        print()

def backtr_rec(mat, n, line = 0, col = 0):
    for comp in [0, 1]:
        mat[line][col] = comp
        if consistent(mat, line, col):
            if solution(n, line, col):
                solutionFound(mat, n)
            else:
                if col + 1 == n:
                    backtr_rec(mat, n, line + 1, 0)
                else:
                    backtr_rec(mat, n, line, col + 1)

def main():
    n = int(input('n = '))
    mat = [[None for col in range(n)] for line in range(n)]
    backtr_rec(mat, n)
    global nr_sol
    assert nr_sol == 4 ** (n * (n - 1) // 2)

main()