#2. Se dă un întreg pozitiv, găsiți toate descompunerile în sumă de numere prime.

nr_sol = 0

def eprim(k):
    if k == 2:
        return True
    if k <= 1 or not (k % 2):
        return False
    div = 3
    while div * div <= k:
        if not (k % div):
            return False
        div += 2
    return True

def print_solution(sol):
    global nr_sol
    nr_sol += 1
    print('Solution #', end = '')
    print(nr_sol, end = ': ')
    for idx in range(len(sol) - 1):
        print(sol[idx], end = '+')
    print(sol[-1], end = '\n')

def recursive_back(sol, n, sum):
    for elem in range(2, n - 1):
        if eprim(elem):
            sol.append(elem)
            sum += elem
            if sum == n:
                print_solution(sol)
            elif sum < n:
                recursive_back(sol, n, sum)
            sum -= elem
            sol.pop()

def sum_list(list):
    sum = 0
    for elem in list:
        sum += elem
    return sum

def solution(sol, n):
    return sum_list(sol) == n

def iterative_back(n):
    sol = [1] #candidate solution
    while len(sol) > 0:
        choosed = False
        while not choosed and sum_list(sol) < n and sol[-1] < n - 2:
            if sol[-1] != 1 and sol[-1] % 2:
                sol[-1] += 2 #increase the last component
            else:
                sol[-1] = sol[-1] + 1 #increase the last component
            choosed = eprim(sol[-1])
        if choosed:
            if solution(sol, n):
                print_solution(sol)
            sol.append(1) #expand candidate solution
        else:
            sol = sol[:-1] #go back one component

def pb2():
    print('Enunț problema 2:\nSe dă un întreg pozitiv, găsiți toate descompunerile în sumă de numere prime.', end = '\n\n')
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
    print('\nDescompunerile numarului', n, 'in suma de numere prime sunt:')
    sol = []
    print('\nSolutii varianta recursiva:')
    recursive_back(sol, n, 0)
    global nr_sol
    if not nr_sol:
        print('Nu exista solutii!\nNumarul', n, 'nu poate fi descompus in suma de numere prime!')
    nr_sol = 0
    print('\nSolutii varianta iterativa:')
    iterative_back(n)
    if not nr_sol:
        print('Nu exista solutii!\nNumarul', n, 'nu poate fi descompus in suma de numere prime!')

pb2()