#12. Se dă o listă de numere întregi a1,...an.
#Determinaţi toate posibilităţile de a insera operatorul de + şi – între numere astfel încât rezultatul expresiei este pozitiv.

nr_sol = 0

def esol(sol, a):
    if len(sol) < len(a) - 1:
        return False
    suma = a[0]
    for idx in range(len(sol)):
        if not sol[idx]:
            suma += a[idx + 1]
        else:
            suma -= a[idx + 1]
    return suma >= 0

def afisare_solutie(sol, a):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    print(a[0], end = '')
    sum = a[0]
    for idx in range(1, len(a)):
        if not sol[idx - 1]:
            sum += a[idx]
            print(' + ', end = '')
        else:
            sum -= a[idx]
            print(' - ', end = '')
        if a[idx] >= 0:
            print(a[idx], end = '')
        else:
            print('(', end = '')
            print(a[idx], end = ')')
    print(' = ', sum)

def recursive_back(sol, a):
    for comp in [0, 1]:
        #folosim codificarea:
        #0 - plus (+)
        #1 - minus (-)
        sol.append(comp)
        if esol(sol, a):
            afisare_solutie(sol, a)
        elif len(sol) < len(a) - 1:
            recursive_back(sol, a)
        sol.pop()

def iterative_back(a):
    sol = [-1] #candidate solution
    while len(sol) > 0:
        choosed = False
        while not choosed and len(sol) <= len(a) - 1 and sol[-1] < 1:
            sol[-1] += 1 #increase the last component
            choosed = True
        if choosed:
            if esol(sol, a):
                afisare_solutie(sol, a)
            sol.append(-1) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb12():
    print('Enunț problema 12:\nSe dă o listă de numere întregi a1,...an.\nDeterminaţi toate posibilităţile de a insera operatorul de + şi – între numere astfel încât rezultatul expresiei este pozitiv.\n')
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
    sol = []
    print('\nSolutii varianta recursiva:')
    recursive_back(sol, a)
    global nr_sol
    nr_sol = 0
    if not nr_sol:
        print('Nu exista solutii!')
    print('\nSolutii varianta iterativa:')
    iterative_back(a)
    if not nr_sol:
        print('Nu exista solutii!')

pb12()