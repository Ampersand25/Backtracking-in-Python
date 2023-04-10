#10. Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele cu lungime mai
#mare decât 2 cu proprietatea că: numerele sunt în ordine crescătoare şi numerele
#consecutive au cel puţin o cifră în comun.

nr_sol = 0

def cifra_comuna(a, b):
    #Varianta I (cu vector caracteristic <=> vector boolean de frecvente/aparitii)
    car = [False] * 10
    while a:
        car[a % 10] = True
        a //= 10
    while b:
        if car[b % 10]:
            return True
        b //= 10
    return False

    #Varianta II (brute-force)
    '''
    while b:
        copie_a = a
        while a:
            if a % 10 == b % 10:
                return True
            a //= 10
        a = copie_a
        b //= 10
    return False
    '''

def ebun(a, sol):
    if len(sol) == 1:
        return True
    return (sol[-1] == sol[-2] + 1) and (a[sol[-1]] >= a[sol[-2]]) and (cifra_comuna(a[sol[-1]], a[sol[-2]]))

def afisare_solutie(a, sol):
    global nr_sol
    nr_sol += 1
    print('Solutie #', end = '')
    print(nr_sol, end = ': ')
    for component in sol:
        print(a[component], end = '(')
        print(component, end = ') ')
    print()

def recursive_back(a, sol = []):
    start = (0) if (not len(sol)) else (sol[-1] + 1)

    '''
    if not len(sol):
        start = 0
    else:
        start = sol[-1] + 1
    '''

    for idx in range(start, len(a)):
        sol.append(idx)
        if ebun(a, sol):
            if len(sol) >= 2:
                afisare_solutie(a, sol)
            recursive_back(a, sol)
        sol = sol[:-1] #sol.pop()

def iterative_back(a):
    sol = [-1] #candidate solution
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= len(a) and sol[-1] < len(a) - 1:
            sol[-1] += 1 #increase the last component
            choosed = ebun(a, sol)
        if choosed:
            if len(sol) > 1:
                afisare_solutie(a, sol)
            sol.append(sol[-1]) #expand candidate solution
        else:
            sol = sol[:-1] #sol.pop()
                           #go back one component

def pb10():
    print('Enunț problema 10:\nSe dă o listă de numere întregi a1,...an, determinați toate sub-secvențele cu lungime mai mare decât 2 cu proprietatea că: numerele sunt în ordine crescătoare şi numerele consecutive au cel puţin o cifră în comun.\n')
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
    assert(n >= 0)
    a = [None] * n
    for idx in range(n):
        print('a[', end = '')
        print(idx, end = '] = ')
        try:
            a[idx] = int(input())
        except ValueError as ve:
            print(str(ve))
            return
        except TypeError as te:
            print(str(te))
            return
        except Exception as ex:
            print(str(ex))
            return
    if n <= 1:
        print('\nNu exista solutie!')
        return
    print('\nSolutii varianta recursiva:')
    recursive_back(a)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutii!')
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(a)
    if not nr_sol:
        print('Nu exista solutii!')

pb10()