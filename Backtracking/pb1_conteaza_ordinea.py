#1. Pentru listă de monede cu valorile a1,....,an, și o valoare S.
#Tipăriţi toate modalităţile de a plăti suma S cu monedele disponibile.
#Tipăriți un mesaj dacă suma nu se poate plăti.

nr_sol = 0

def ebun(sol):
    return (True) if (len(sol) == 1) else (not (sol[-1] in sol[:-1]))

def afisare_solutie(a, sol):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for comp in sol:
        print(a[comp], end = ' ')
    print()

def recursive_backtracking(a, S, sol = []):
    for idx in range(len(a)):
        sol.append(idx)
        S -= a[idx]
        if S >= 0 and ebun(sol):
            if not S:
                afisare_solutie(a, sol)
            recursive_backtracking(a, S, sol)
        S += a[idx]
        sol.pop()

def suma_solutie(a, sol):
    sum = 0
    for comp in sol:
        sum += a[comp]
    return sum

def esol(a, S, sol):
    return suma_solutie(a, sol) == S

def iterative_backtracking(a, S):
    sol = [-1]
    while len(sol) >= 1:
        choosed = False
        while not choosed and len(sol) <= len(a) and sol[-1] < len(a) - 1:
            sol[-1] += 1
            choosed = ebun(sol)
        if choosed:
            if esol(a, S, sol):
                afisare_solutie(a, sol)
            sol.append(-1)
        else:
            sol = sol[:-1]

def pb1_conteaza_ordinea():
    '''
    Exemple:

    I
    Date de intrare:
    7
    3 8 5 1 10 5 6
    11

    Date de iesire (rezultate):
    Solutia #1: 3 8
    Solutia #2: 8 3
    Solutia #3: 5 1 5
    Solutia #4: 5 5 1
    Solutia #5: 5 6
    Solutia #6: 1 5 5
    Solutia #7: 1 10
    Solutia #8: 1 5 5
    Solutia #9: 10 1
    Solutia #10: 5 5 1
    Solutia #11: 5 1 5
    Solutia #12: 5 6
    Solutia #13: 6 5
    Solutia #14: 6 5

    II
    Date de intrare:
    2
    3 3
    6

    Date de iesire (rezultate):
    Solutia #1: 3 3
    Solutia #2: 3 3

    III
    Date de intrare:
    4
    4 6 3 5
    9

    Date de iesire (rezultate):
    Solutia #1: 4 5
    Solutia #2: 6 3
    Solutia #3: 3 6
    Solutia #4: 5 4

    IV
    Date de intrare:
    5
    4 6 1 9 5
    8

    Date de iesire (rezultate):
    Nu exista solutie!
    Suma 8 nu se poate plati cu monedele disponibile!
    '''

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
    assert n >= 0
    if not n:
        return
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
        assert a[idx] > 0 #assert a[idx] >= 1
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
    assert S >= 0
    if not S:
        return
    print('\nSolutii varianta recursiva:')
    recursive_backtracking(a, S)
    global nr_sol
    if not nr_sol:
        print('\nNu exista solutie!\nSuma', S, 'nu se poate plati cu monedele disponibile!')
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(a, S)
    if not nr_sol:
        print('\nNu exista solutie!\nSuma', S, 'nu se poate plati cu monedele disponibile!')

pb1_conteaza_ordinea()