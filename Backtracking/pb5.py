#5. Generați bilete la PRONOSPORT pentru un bilet cu N meciuri.
#Pronosticurile pentru un meci pot fi 1,X,2.
#Generați toate variantele astfel încât: pronosticul de la ultimul meci nu poate fi X
#și există un maxim de două meciuri cu pronosticul 1.

nr_sol =  0

def esol(sol, N):
    return (False) if (len(sol) != N) else sol[-1] != 'X'

    '''
    if len(sol) != N:
        return False
    return sol[-1] != 'X'
    '''

def print_solution(sol):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for comp in sol:
        print(comp, end = '')
    print()

def recursive_back(sol, N, nr_meciuri_pron_1):
    domain = (1, 'X', 2)
    for component in domain:
        sol.append(component)
        if component == 1:
            nr_meciuri_pron_1 += 1
        if nr_meciuri_pron_1 <= 2:
            if esol(sol, N):
                print_solution(sol)
            elif len(sol) < N:
                recursive_back(sol, N, nr_meciuri_pron_1)
        sol.pop()
        if component == 1:
            nr_meciuri_pron_1 -= 1

def consistent(sol):
    cont = 0
    for comp in sol:
        if comp == 1:
            cont += 1
    return cont <= 2

def iterative_back(N):
    sol = [None] #candidate solution
    symbols_list = [-1]
    symbols = (1, 'X', 2)
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= N and symbols_list[-1] < 2: #while not choosed and len(symbols_list) <= N and symbols_list[-1] < 2:
            symbols_list[-1] += 1 #increase the last component
            sol[-1] = symbols[symbols_list[-1]] #sol[-1] == sol[len(sol) - 1]
            choosed = consistent(sol)
        if choosed:
            if esol(sol, N):
                print_solution(sol)
            sol.append(None) #expand candidate solution
            symbols_list.append(-1)
        else:
            sol = sol[:-1] #go back one component
            symbols_list = symbols_list[:-1]

def pb5():
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
    recursive_back(sol, N, 0)
    global nr_sol
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(N)

pb5()