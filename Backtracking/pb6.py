#6. Se dă o listă de numere întregi a1,...,an.
#Generați toate sub-secvențele cu proprietatea că suma numerelor este divizibilă cu N dat.

nr_sol = 0

def ebun(sol, step):
    #ternary operator:
    #[on_true] if [expression] else [on_false]
    return (True) if (step == 1) else (sol[step] == sol[step - 1] + 1)

    '''
    if step == 1:
        return True
    return sol[step] == sol[step - 1] + 1
    '''

def esol(a, N, sol, step):
    sum = 0
    for idx in range(1, step + 1):
        sum += a[sol[idx]]
    return not (sum % N)

def print_sol(a, sol, step):
    print('[', end = '')
    for idx in range(1, step):
        print(a[sol[idx]], end = ', ')
    print(a[sol[step]], end = ']\n')

def recursive_backtracking(a, N, sol, step):
    for idx in range(sol[step - 1] + 1, len(a)):
        sol[step] = idx
        if ebun(sol, step):
            if esol(a, N, sol, step):
                global nr_sol
                nr_sol += 1
                print('Solutia #', end = '')
                print(nr_sol, end = ': ')
                print_sol(a, sol, step)
            if step < len(a) - 1:
                recursive_backtracking(a, N, sol, step + 1)

def slice_list(list, start_idx, finish_idx):
    return list[(start_idx):(finish_idx + 1)]

def compute_sum_list(list):
    sum = 0
    for elem in list:
        sum += elem
    return sum

def iterative_backtracking(a, N):
    n = len(a)
    for start in range(1, n):
        for finish in range(start, n):
            subsecv = slice_list(a, start, finish)
            sum_list = compute_sum_list(subsecv)
            if not (sum_list % N):
                global nr_sol
                nr_sol += 1
                print('Solutia #', end = '')
                print(nr_sol, end = ': ')
                print(subsecv)

def pb6():
    print('Enunț problema 6:\nSe dă o listă de numere întregi a1,...,an.\nGenerați toate sub-secvențele cu proprietatea că suma numerelor este divizibilă cu N dat.', end = '\n\n')
    n = int(input('n = '))
    assert(n >= 1)
    a = [None] * (n + 1)
    for idx in range(1, n + 1):
        print('a[', end = '')
        print(idx, end = ']: ')
        a[idx] = int(input())
    N = int(input('N = '))
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(a, N)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutii!')
    print('\nSolutii varianta recursiva:')
    sol = [0] * (n + 1)
    nr_sol = 0
    recursive_backtracking(a, N, sol, 1)
    if not nr_sol:
        print('Nu exista solutii!')

pb6()