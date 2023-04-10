#13. Se dă o listă de numere întregi a1,...an. Generaţi toate permutările listei pentru care
#numerele au aspect de munte (cresc până la un punct de unde descresc).
#Ex. 10, 16, 27, 18, 14, 7.

nr_sol = 0

def ebun(sol):
    #ternary operator (operatorul ternar)
    return True if len(sol) == 1 else not (sol[-1] in sol[:-1])

def esol(a, sol):
    if len(sol) != len(a): #if len(sol) < len(a):
        return False
    cresc = descresc = False #cresc, descresc = False, False
    for idx in range(1, len(sol)):
        if a[sol[idx]] > a[sol[idx - 1]]:
            if descresc:
                return False
            cresc = True
        if a[sol[idx]] < a[sol[idx - 1]]:
            if not cresc:
                return False
            descresc = True
    return cresc and descresc

def afisare_solutie(a, sol):
    global nr_sol
    nr_sol += 1
    print('Solutia #', end = '')
    print(nr_sol, end = ': ')
    for component in sol:
        print(a[component], end = ' ')
    print(end = '\n')

def recursive_backtr(a, sol = []):
    for comp in range(len(a)):
        sol.append(comp)
        if ebun(sol):
            if esol(a, sol):
                afisare_solutie(a, sol)
            elif len(sol) < len(a):
                recursive_backtr(a, sol)
        sol.pop()

def iterative_backtr(a):
    sol = [-1] #candidate solution
    while len(sol):
        choosed = False
        while not choosed and len(sol) <= len(a) and sol[-1] < len(a) - 1:
            sol[-1] += 1 #increase the last component
            choosed = ebun(sol)
        if choosed:
            if esol(a, sol):
                afisare_solutie(a, sol)
            sol.append(-1) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb13():
    print('Enunț problema 13:\nSe dă o listă de numere întregi a1,...an.\nGeneraţi toate permutările listei pentru care numerele au aspect de munte (cresc până la un punct de unde descresc).\nEx. 10, 16, 27, 18, 14, 7.\n')
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
        return
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
    print('\nSolutii varianta recursiva:')
    recursive_backtr(a)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutie!')
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_backtr(a)
    if not nr_sol:
        print('Nu exista solutie!')

pb13()