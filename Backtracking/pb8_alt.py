#8. Generați toate sub-secvențele de lungime 2n+1, formate din 0, -1 și 1, astfel încât
#a1 = 0, ..., a2n+1 = 0 și |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n.

nr_sol = 0

def consistent(n, sol):
    if len(sol) == 2 * n and not sol[-1]:
        return False
    return sol[-1] != sol[-2]

def solution(n, sol):
    return len(sol) == 2 * n

def solutionFound(sol, varianta = 'recursiva'):
    global nr_sol
    nr_sol += 1

    print('Solutia (varianta recursiva) #', end='') if varianta == 'recursiva' else print('Solutia (varianta iterativa) #', end = '')

    '''
    if varianta == 'recursiva':
        print('Solutia (varianta recursiva) #', end = '')
    else:
        print('Solutia (varianta iterativa) #', end = '')
    '''

    print(nr_sol, end = ': ')
    for idx in range(len(sol) - 1):
        print(sol[idx], end = ', ')
    print(sol[-1]) #print(sol[len(sol) - 1], end = '\n')

def recursive_backtracking(n, sol = [0]):
    for component in [-1, 0, 1]: #for component in range(-1, 2):
        sol.append(component)
        if consistent(n, sol):
            if solution(n, sol):
                sol.append(0)
                solutionFound(sol)
                sol.pop()
            else:
                recursive_backtracking(n, sol)
        sol.pop()

def iterative_backtracking(n):
    sol = [0, -2] #candidate solution
    while len(sol) > 1: #while len(sol) >= 2:
                        #while len(sol) != 1:
        choosed = False
        while not choosed and len(sol) <= 2 * n and sol[-1] <= 0:
            sol[-1] = sol[-1] + 1 #increase the last component
            choosed = consistent(n, sol)
        if choosed:
            if solution(n, sol):
                sol.append(0)
                solutionFound(sol, varianta = 'iterativa')
                sol.pop()
            sol.append(-2) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb8_alt():
    #0, ..., -1, -1, ..., 0 - NU (|(-1) - (-1)| = |-1 - (-1)| = |-1 + 1| = |0| = 0)
    #0, ..., -1,  0, ..., 0 - DA (|0 - (-1)| = |0 + 1| = |1| = 1)
    #0, ..., -1,  1, ..., 0 - DA (|1 - (-1)| = |1 + 1| = |2| = 2)

    #0, ...,  0, -1, ..., 0 - DA (|(-1) - 0| = |-1 - 0| = |-1| = 1)
    #0, ...,  0,  0, ..., 0 - NU (|0 - 0| = |0| = 0)
    #0, ...,  0,  1, ..., 0 - DA (|1 - 0| = |1| = 1)

    #0, ...,  1, -1, ..., 0 - DA (|(-1) - 1| = |-1 - 1| = |-2| = 2)
    #0, ...,  1,  0, ..., 0 - DA (|0 - 1| = |-1| = 1)
    #0, ...,  1,  1, ..., 0 - NU (|1 - 1| = |0| = 0)

    #Conditie de corectitudine a unei secvente:
    #nu avem voie sa avem -1 urmat de -1
    #nu avem voie sa avem 0 urmat de 0
    #nu avem voie sa avem 1 urmat de 1
    #=> nu avem voie sa avem doua elemente egale pe pozitii consecutive (succesive)

    #Asadar, trebuie ca:
    #1. a1 = a2n+1 = 0
    #2. |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n
    #   |a(i+1) - ai| != 0     , pentru orice i, 1 <= i <= 2n
    #   a(i+1) - ai != 0       , pentru orice i, 1 <= i <= 2n
    #   a(i+1) != ai           , pentru orice i, 1 <= i <= 2n

    print('Enunț problema 8:\nGenerați toate sub-secvențele de lungime 2n+1, formate din 0, -1 și 1, astfel încât a1 = 0, ..., a2n+1 = 0 și |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n.\n')
    try:
        n = int(input('n = '))
    except ValueError as ve:
        print(str(ve))
        return
    except TypeError as te:
        print(str(te))
        return
    except Exception as ex:
        print(str(ex))
        return
    assert n >= 0
    if not n:
        print('\nSolutii varianta recursiva:\nSolutia (varianta recursiva) #1: 0')
        print('\nSolutii varianta iterativa:\nSolutia (varianta iterativa) #1: 0')
        return #exit(0)
    print('\nSolutii varianta recursiva:')
    recursive_backtracking(n)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutie!')
    else:
        nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(n)
    if not nr_sol:
        print('Nu exista solutie!')

pb8_alt()