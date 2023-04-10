#6. Se dă o listă de numere întregi a1,...,an.
#Generați toate sub-secvențele cu proprietatea că suma numerelor este divizibilă cu N dat.

nr_sol_rec = nr_sol_iter = False

def ebun(sol):
    #pentru generare de subsiruriri
    '''
    return True
    '''

    #pentru generare de subsecvente
    return True if len(sol) == 1 else sol[-1] == sol[-2] + 1

def esol(a, N, sol):
    sum = 0
    for idx in range(len(sol)):
        sum += a[sol[idx]]
    return not (sum % N)

def afisare_solutie(a, sol, metoda = 'recursiv'):
    if metoda == 'recursiv':
        global nr_sol_rec
        nr_sol_rec += 1
        print('Solutia recursiva #', end = '')
        print(nr_sol_rec, end = ': ')
    else:
        global nr_sol_iter
        nr_sol_iter += 1
        print('Solutia iterativa #', end='')
        print(nr_sol_iter, end=': ')
    for comp in sol[:-1]:
        print(a[comp], end = '(')
        print(comp, end = '), ')
    print(a[sol[-1]], end = '(')
    print(sol[-1], end = ')\n')

def recursive_backtracking(a, N, sol = [], sum = 0):
    start = 0 if not len(sol) else sol[-1] + 1
    for component in range(start, len(a)):
        sol.append(component)
        sum += a[component] #sum += a[sol[-1]]
        if ebun(sol):
            if not (sum % N):
                afisare_solutie(a, sol)
            if len(sol) < len(a):
                recursive_backtracking(a, N, sol, sum)
        sum -= a[component] #sum -= a[sol[-1]]
        sol.pop()

def iterative_backtracking(a, N):
    sol = [-1] #candidate solution
    while len(sol) > 0: #while len(sol):
        ales = False
        while not ales and len(sol) <= len(a) and sol[-1] < len(a) - 1:
            sol[-1] += 1 #increase the last component
            ales = ebun(sol)
        if not ales:
            sol = sol[:-1] #go back one component
        else:
            if esol(a, N, sol):
                afisare_solutie(a, sol, metoda = 'iterativ')
            sol.append(sol[-1]) #expand candidate solution

def pb6_var_alt():
    print('Enunț problema 6:\nSe dă o listă de numere întregi a1,...,an.\nGenerați toate sub-secvențele cu proprietatea că suma numerelor este divizibilă cu N dat.', end = '\n\n')
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
    try:
        N = int(input('N = '))
    except ValueError as ve:
        print(ve)
        return
    except TypeError as te:
        print(te)
        return
    except Exception as ex:
        print(ex)
        return
    print('\nSolutii varianta recursiva:')
    recursive_backtracking(a, N)
    global nr_sol_rec
    if not nr_sol_rec:
        print('Nu exista solutie!')
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(a, N)
    global nr_sol_iter
    if not nr_sol_iter:
        print('Nu exista solutie!')
    assert nr_sol_rec == nr_sol_iter

pb6_var_alt()