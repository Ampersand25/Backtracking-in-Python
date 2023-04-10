#5. Generați bilete la PRONOSPORT pentru un bilet cu N meciuri.
#Pronosticurile pentru un meci pot fi 1,X,2.
#Generați toate variantele astfel încât: pronosticul de la ultimul meci nu poate fi X
#și există un maxim de două meciuri cu pronosticul 1.

nr_sol =  0

def ebun(sol):
    cont = 0
    for idx in range(len(sol)):
        cont += (1) if (sol[idx] == 1) else (0)
    return cont <= 2

def esol(sol, N, method = 'recursive'):
    if method == 'recursive':
        return (False) if (len(sol) != N) else sol[-1] != 'X'
    return (False) if (len(sol) != N) else sol[-1] != 3

    '''
    if len(sol) != N:
        return False
    if method == 'recursive':
        return sol[-1] != 'X'
    return sol[-1] != 3
    '''

def type_solution(sol, method = 'recursive'):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for comp in sol:
        if comp == 1 or comp == 2 or comp == 'recursive':
            print(comp, end='')
        else:
            print(end = 'X')
    print()

def recursive_back(sol, N):
    domain = (1, 'X', 2)
    for component in domain:
        sol.append(component)
        if ebun(sol):
            if esol(sol, N):
                type_solution(sol)
            elif len(sol) < N:
                recursive_back(sol, N)
        sol.pop()

def iterative_back(N):
    sol = [0] #candidate solution
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= N and sol[-1] < 3:
            sol[-1] += 1 #increase the last component
            choosed = ebun(sol)
        if choosed:
            if esol(sol, N, method = 'iterative'):
                type_solution(sol, method = 'iterative')
            sol.append(0) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb5_alt():
    print('Enunț problema 5:\nGenerați bilete la PRONOSPORT pentru un bilet cu N meciuri.\nPronosticurile pentru un meci pot fi 1,X,2.\nGenerați toate variantele astfel încât: pronosticul de la ultimul meci nu poate fi X și există un maxim de două meciuri cu pronosticul 1.', end = '\n\n')
    try:
        N = int(input('N = '))
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except Exception as ex:
        print(ex)
    assert N >= 0
    sol = []
    print('\nSolutii varianta recursiva:')
    recursive_back(sol, N)
    global nr_sol
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(N)

pb5_alt()