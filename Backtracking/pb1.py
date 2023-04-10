#1. Pentru listă de monede cu valorile a1,....,an, și o valoare S.
#Tipăriţi toate modalităţile de a plăti suma S cu monedele disponibile.
#Tipăriți un mesaj dacă suma nu se poate plăti.

nr_sol = 0

def print_solution(sol, a, S, varianta = 'recursiva'):
    global nr_sol
    nr_sol += 1
    if nr_sol == 1:
        if varianta == 'recursiva':
            print('\nModalitatile de plata a sumei', S, 'cu monedele introduse sunt:')
        print('\nSolutii varianta', varianta, end = ':\n')
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    temp = []
    for idx in range(len(sol)):
        if sol[idx]:
            temp.append(a[idx])
    for idx in range(len(temp) - 1):
        print(temp[idx], end = ' + ')
    print(temp[-1], end = ' = ')
    print(S)

def recursive_back(sol, a, S, value = 0):
    for component in [True, False]:
        sol.append(component)
        value += sol[-1] * a[len(sol) - 1]
        if value <= S:
            if len(sol) == len(a) and value == S:
                print_solution(sol, a, S)
            elif len(sol) < len(a):
                recursive_back(sol, a, S, value)
        value -= sol[-1] * a[len(sol) - 1]
        sol.pop()

def sum_candidate_sol(sol, a):
    sum = 0
    for idx in range(len(sol)):
        sum += sol[idx] * a[idx]
    return sum

def consistent(sol, a, S):
    return sum_candidate_sol(sol, a) <= S

def solution(sol, a, S):
    if len(sol) < len(a): #if len(sol) != len(a):
        return False
    return sum_candidate_sol(sol, a) == S

def iterative_back(a, S):
    sol = [2]
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= len(a) and sol[-1] > 0:
            sol[-1] -= 1
            choosed = consistent(sol, a, S)
        if choosed:
            if solution(sol, a, S):
                print_solution(sol, a, S, varianta = 'iterativa')
            sol.append(2)
        else:
            sol = sol[:-1]

def pb1():
    print('Enunț problema 1:\nPentru listă de monede cu valorile a1,....,an, și o valoare S.\nTipăriţi toate modalităţile de a plăti suma S cu monedele disponibile.\nTipăriți un mesaj dacă suma nu se poate plăti.', end = '\n\n')
    try:
        n = int(input('n = '))
    except ValueError as ve:
        print(ve)
        return
    except TypeError as te:
        print(te)
        return
    except Exception as ex:
        print(ex)
        return
    assert(n >= 0)
    if not n:
        exit(0)
    a = [None] * n
    for idx in range(n):
        print('a[', end = '')
        print(idx, end = '] = ')
        try:
            a[idx] = int(input())
        except ValueError as ve:
            print(ve)
            return
        except TypeError as te:
            print(te)
            return
        except Exception as ex:
            print(ex)
            return
        assert(a[idx] > 0) #assert(a[idx] >= 1)
    try:
        S = int(input('S = '))
    except ValueError as ve:
        print(ve)
        return
    except TypeError as te:
        print(te)
        return
    except Exception as ex:
        print(ex)
        return
    assert(S >= 0)
    if not S:
        exit(0)
    sol = []
    recursive_back(sol, a, S)
    global nr_sol
    if not nr_sol:
        print('\nNu exista solutie!\nSuma', S, 'nu se poate plati cu monedele disponibile!')
        exit(0)
    nr_sol = 0
    iterative_back(a, S)

pb1()