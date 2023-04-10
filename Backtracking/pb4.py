#4. Se dă o listă de numere întregi a1,...an,
#determinați toate sub-secvențele (ordinea elementelor este menținută) strict crescătoare.

nr_sol = 0

def ebun(sol, a):
    return True if len(sol) == 1 else sol[-1] == sol[-2] + 1 and a[sol[-1]] > a[sol[-2]]

def type_sol(sol, a):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for component in sol:
        print(a[component], end = '(')
        print(component, end = ') ')
    print()

def recursive_backtr(sol, a):
    for elem in range(len(a)):
        sol.append(elem)
        if ebun(sol, a):
            type_sol(sol, a)
            if len(sol) < len(a):
                recursive_backtr(sol, a)
        sol.pop()

def iterative_backtr(a):
    sol = [-1] #candidate solution
    while len(sol) > 0:
        ales = False
        while not ales and len(sol) <= len(a) and sol[-1] < len(a) - 1:
            sol[-1] += 1 #increase the last component
            ales = ebun(sol, a)
        if ales:
            type_sol(sol, a)
            sol.append(-1) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb4():
    print('Enunț problema 4:\nSe dă o listă de numere întregi a1,...an, determinați toate sub-secvențele (ordinea elementelor este menținută) strict crescătoare.', end = '\n\n')
    try:
        n = int(input('n = '))
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except Exception as ex:
        print(ex)
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
        except TypeError as te:
            print(te)
        except Exception as ex:
            print(ex)
    print('\nToate sub-secventele strict crescatoare din sirul a sunt:')
    sol = []
    print('\nSolutii varianta recursiva:')
    recursive_backtr(sol, a)
    global nr_sol
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_backtr(a)

pb4()