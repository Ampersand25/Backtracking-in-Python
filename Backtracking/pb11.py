#11. Se dau două numere naturale m şi n.
#Generaţi liste formate din numere de la 1 la n cu proprietatea că
#diferenţa (în valoare absolută) între două numere consecutive din listă este m.
#Tipăriţi un mesaj dacă problema nu are soluţie.

nr_sol = 0

def ebun(m, sol):
    return True if len(sol) == 1 else abs(sol[-1] - sol[-2]) == m and not (sol[-1] in sol[:-1])

    '''
    if len(sol) == 1:
        return True
    return abs(sol[-1] - sol[-2]) == m and not (sol[-1] in sol[:-1])
    '''

def esol(sol):
    return len(sol) > 1 #return len(sol) >= 2

def afiseaza_solutie(sol):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for component in sol:
        print(component, end = ' ')
    print()

def recursive_back(n, m, sol = []):
    for comp in range(1, n + 1):
        sol.append(comp)
        if ebun(m, sol):
            if esol(sol):
                afiseaza_solutie(sol)
            recursive_back(n, m, sol)
        sol.pop()

def iterative_back(n, m):
    sol = [0] #candidate solution
    while len(sol): #while len(sol) != 0:
        gasit = False
        while not gasit and len(sol) <= n and sol[-1] < n:
            sol[-1] += 1 #increase the last component
            gasit = ebun(m, sol)
        if not gasit:
            sol = sol[:-1] #go back one component
        else:
            if esol(sol):
                afiseaza_solutie(sol)
            sol.append(0) #expand candidate solution

def pb11():
    print('Enunț problema 11:\nSe dau două numere naturale m şi n.\nGeneraţi liste formate din numere de la 1 la n cu proprietatea că diferenţa (în valoare absolută) între două numere consecutive din listă este m.\nTipăriţi un mesaj dacă problema nu are soluţie.\n')
    try:
        m = int(input('m = '))
    except ValueError as ve:
        print(ve)
        return
    except TypeError as te:
        print(te)
        return
    except Exception as ex:
        print(ex)
        return
    assert m >= 0
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
    print('\nSolutii varianta recursiva:')
    recursive_back(n, m)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutie!')
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(n, m)
    if not nr_sol:
        print('Nu exista solutie!')

pb11()