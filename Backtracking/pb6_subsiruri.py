nr_sol = 0

def solutionFound(a, sol):
    global nr_sol
    nr_sol += 1
    print('Solutia cu numarul', nr_sol, end = ': ')
    for idx in range(len(sol)): #for idx in range(len(a)):
        if sol[idx]:
            print(a[idx], end = '(')
            print(idx, end = ') ')
    print() #print(end = '\n')

def recursive_back(a, N, sol = [], sum = 0):
    for comp in [0, 1]: #for comp in range(0, 2):
        sol.append(comp)
        sum += a[len(sol) - 1] * comp #sum += a[len(sol) - 1] * sol[-1]
        if len(sol) == len(a):
            if 1 in sol and not (sum % N):
                solutionFound(a, sol)
        else: #elif len(sol) < len(a):
            recursive_back(a, N, sol, sum)
        sum -= a[len(sol) - 1] * comp #sum -= a[len(sol) - 1] * sol[-1]
        sol.pop()

def iterative_back(a, N, sum = 0):
    sol = [-1]
    while len(sol) > 0: #while len(sol) != 0:
        choosed = False
        while not choosed and len(sol) <= len(a) and sol[-1] < 1:
            sol[-1] += 1
            choosed = True
        if choosed:
            if sol[-1]:
                sum += a[len(sol) - 1]
            if len(sol) == len(a) and 1 in sol and not (sum % N):
                solutionFound(a, sol)
            sol.append(-1)
        else:
            if len(sol) <= len(a) and sol[-1]:
                sum -= a[len(sol) - 1]
            sol = sol[:-1] #sol.pop()

def pb6_subsiruri():
    n = int(input('n = '))
    a = []
    for idx in range(n):
        print('a[', end = '')
        print(idx, end = ']: ')
        elem = int(input())
        a.append(elem)
    N = int(input('N = '))
    print('\nSolutii varianta recursiva:')
    recursive_back(a, N)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutii!')
    else:
        nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(a, N)
    if not nr_sol:
        print('Nu exista solutii!')

pb6_subsiruri()