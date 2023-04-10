#14. Se dă o listă de numere întregi a1,...an. Generaţi toate permutările listei pentru care
#numerele au aspect de vale (descresc până la un punct de unde cresc).

nr_sol_rec = nr_sol_iter = 0

def ebun(sol):
    #Varianta I
    #ternary operator (operatorul ternar)
    return not (sol[-1] in sol[:-1])

    #Varianta II
    '''
    for idx in range(len(sol) - 1):
        if sol[idx] == sol[-1]: #if sol[idx] == sol[len(sol) - 1]:
            return False
    return True
    '''

    #Varianta III
    '''
    for comp in sol[:-1]:
        if comp == sol[-1]: #if comp == sol[len(sol) - 1]:
            return False
    return True
    '''

def esol(a, sol):
    cresc = descresc = False #cresc, descresc = False, False
    for idx in range(1, len(sol)):
        if a[sol[idx - 1]] > a[sol[idx]]:
            if cresc:
                return False
            descresc = True
        if a[sol[idx - 1]] < a[sol[idx]]:
            if not descresc:
                return False
            cresc = True
    return cresc #return cresc and descresc

def afisare_solutie(a, sol, varianta = 'recursiva'):
    if varianta == 'recursiva':
        global nr_sol_rec
        nr_sol_rec += 1
        print('Solutia varianta recursiva #', end = '')
        print(nr_sol_rec, end = ': ')
    else:
        global nr_sol_iter
        nr_sol_iter += 1
        print('Solutia varianta iterativa #', end='')
        print(nr_sol_iter, end=': ')
    #se pp verificat ca len(a) == len(sol)
    for idx in range(len(sol)): #for idx in range(len(a)):
        print(a[sol[idx]], end = ' ')
    print()

def recursive_backtr(a, sol = []):
    for comp in range(len(a)):
        sol.append(comp)
        if ebun(sol):
            if len(sol) == len(a) and esol(a, sol):
                afisare_solutie(a, sol)
            elif len(sol) != len(a):
                recursive_backtr(a, sol)
        sol.pop()

def iterative_backtr(a):
    sol = [-1] #candidate solution
    while len(sol) >= 1: #while len(sol) > 0:
        ales = False
        while not ales and sol[len(sol) - 1] < len(a) - 1:
            sol[len(sol) - 1] += 1 #increase the last component
            ales = ebun(sol)
        if not ales:
            sol.pop() #go back one component
        else:
            if esol(a, sol):
                afisare_solutie(a, sol, varianta = 'iterativa')
            sol.append(-1) #expand candidate solution

def pb14():
    print('Enunț problema 14:\nSe dă o listă de numere întregi a1,...an.\nGeneraţi toate permutările listei pentru care numerele au aspect de vale (descresc până la un punct de unde cresc).\n')
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
    global nr_sol_rec
    if not nr_sol_rec:
        print('Nu exista solutie!')
    print('\nSolutii varianta iterativa:')
    iterative_backtr(a)
    global nr_sol_iter
    if not nr_sol_iter:
        print('Nu exista solutie!')
    assert nr_sol_rec == nr_sol_iter

pb14()