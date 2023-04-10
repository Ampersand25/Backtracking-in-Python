#3. Generați toate permmutările de dimensiune n (1..n), cu propritatea că
#pentru orice i 2<=i<=n exista un j, 1<=j<=i astfel încât |v(i)-v(j)|=1.

nr_sol = 0

def ebun(sol):
    #Varianta I
    '''
    ok = True if len(sol) == 1 else False
    for idx in range(len(sol) - 1):
        if sol[idx] == sol[-1]:
            return False
        if abs(sol[-1] - sol[idx]) == 1:
            ok = True
    return ok
    '''

    #Varianta II
    if len(sol) == 1:
        return True
    ok = False
    for comp in sol[:-1]:
        if comp == sol[-1]:
            return False
        if abs(comp - sol[-1]) == 1:
            ok = True
    return ok

def esol(sol, n):
    return len(sol) == n

def print_sol(sol):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for idx in range(len(sol) - 1):
        print(sol[idx], end = ', ')
    print(sol[-1])

def recursive_backtracking(sol, n):
    for comp in range(1, n + 1):
        sol.append(comp)
        if ebun(sol):
            if esol(sol, n):
                print_sol(sol)
            else: #elif len(sol) < n:
                recursive_backtracking(sol, n)
        sol.pop()

def iterative_backtracking(n):
    sol = [0] #candidate solution
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= n and sol[-1] < n:
            sol[-1] += 1 #increase the last component
            choosed = ebun(sol)
        if choosed:
            if esol(sol, n):
                print_sol(sol)
            sol.append(0) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb3():
    print('Enunț problema 3:\nGenerați toate permmutările de dimensiune n (1..n), cu propritatea că pentru orice i 2<=i<=n exista un j, 1<=j<=i astfel încât |v(i)-v(j)|=1.', end = '\n\n')
    try:
        n = int(input('n = '))
    except ValueError as ve:
        print(str(ve))
    except TypeError as te:
        print(str(te))
    except Exception as ex:
        print(str(ex))
    assert n >= 1
    sol = []
    print('\nSolutii varianta recursiva:')
    recursive_backtracking(sol, n)
    global nr_sol
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(n)

pb3()