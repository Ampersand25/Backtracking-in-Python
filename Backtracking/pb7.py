#7. Pentru un n dat generați toate secvențele de paranteze care se închid corect.
#Examplu: n=4
#două soluții: (()) și ()()

nr_sol = 0 #variabila de tip contor care sa retina numarul solutiilor generate

def ebun(sol, step):
    #functie operand care verifica daca componenta de pe pozitia step din solutia candidat sol (reprezentata ca si o lista booleana) este sau nu valida
    #date de intrare: sol  - lista de numere (solutia candidat)
    #                 step - numar intreg (pozitia ultimei componente generate din solutia candidat)
    #date de iesire: False - componenta de la indicele step din sol nu este buna (se va inlocui cu o alta componenta daca nu s-a epuizat tot spatiul componentelor, in caz contrar se va face bakc-track in functi)
    #                True  - componenta de la indicele step din sol este buna (se va pastra si se va genera urmatoarea componenta din solutia candidat)

    cont = 0 #variabila in care vom memora diferenta: nr paranteze deschise - nr paranteze inchise
    #avem 3 situatii posibile
    #cont == 0 => avem la fel de multe paranteze deschise ca si inchise => OK
    #cont  < 0 => avem mai multe paranteze inchise decat deschise => NOT OK (nu mai putem deschide parantezele inchise)
    #cont  > 0 => avem mai multe paranteze deschise decat inchise => OK (parantezele inchise mai pot fi inchise)
    for idx in range(step + 1): #parcurgem toate componentele generate pana la pasul step
        if not sol[idx]: #paranteza deschisa
            cont += 1 #increment
        else: #paranteza inchisa
            cont -= 1 #decrement
        if cont < 0: #avem mai multe paranteze inchise decat deschise
            return False #componenta sol[step] nu este valida
    return True #componenta sol[step] este valida

def esol(sol, step, n):
    #functie care verifica daca o solutie candidat este sau nu solutie
    #date de intrare: sol  - lista de intregi: sirul solutie
    #                 step - intreg: pozitia din lista a ultimei componente generate
    #                 n    - intreg: numarul de componente care trebuie generat (lungimea unei solutii)
    #date de iesire: False - solutia sol nu este fezabila
    #                True  - solutia sol este fezabila

    if step < n: #solutia candidat are n componente (paranteze)
        return False #solutia candidat nu este solutie fezabila
    cont = 0 #variabila in care vom retine diferenta dintre numarul parantezelor deschise si cel al parantezelor inchise din solutia candidat sol
    for comp in sol: #parcurgem iterativ fiecare componenta din vectorul solutie
        if not comp: #paranteza deschisa
            cont += 1 #am gasit o paranteza deschisa
        else: #paranteza inchisa
            cont -= 1 #am gasit o paranteza inchisa
        if cont < 0: #exista mai multe paranteze inchise decat deschise => solutia nu este fezabila
            return False
    return not cont #trebuie ca numarul parantezelor deschise sa fie egal cu cel al parantezelor inchise (adica diferenta lor sa fie 0)

def print_solution(sol):
    #procedura (functie procedurala = care nu returneaza nimic) care afiseaza o solutie a problemei, o secventa de paranteze corect construita
    #date de intrare: sol - lista de intregi (0 si 1)
    #date de iesire: -

    global nr_sol #nr_sol - variabila declarata global (o importam in functie cu ajutorul directivei global)
    nr_sol += 1 #marcam faptul ca am gasit o noua solutie
    print('Solution #', end = '')
    print(nr_sol, end = ': ')
    for component in sol:
        #component == 0 => paranteza deschisa
        #             1 => paranteza inchisa
        if not component: #if component == 0
            print('(', end = '') #paranteza deschisa
        else: #elif component == 1
            print(')', end = '') #paranteza inchisa
    print() #simulam trecerea la rand nou

def recursive_backtracking(sol, step):
    #varianta recursiva/recurenta de backtracking, care se apeleaza pe ea insasi (contine auto-apeluri)
    #procedura printeaza pe ecran (la iesirea standard) toate secventele corect parantezate de lungime n
    #date de intrare: sol  - vectorul solutie (lista booleana: contine doar 0 si 1)
    #                 step - intreg (reprezinta pozitia celei mai recente componente generate in solutia candidat sol)
    #date de iesire: -

    for elem in [0, 1]: #for elem in range(0, 2):
        sol[step] = elem
        if ebun(sol, step): #validam componenta curenta (cea de pe pozitia step din sol)
            if esol(sol, step, len(sol) - 2): #verificam daca s-a obtinut o solutie (daca solutia candidat este solutie fezabila)
                print_solution(sol) #afisam solutia gasita in caz afirmativ
            elif step < len(sol) - 2: #nu s-au generat n - 2 paranteze, unde n reprezinta lungimea sirului sol (adica len(sol))
                recursive_backtracking(sol, step + 1) #se continua generarea cu o noua componenta (se incrementeaza continutul lui step)

def iterative_backtracking(n):
    #varianta iterativa de backtracking (non-recursiva), care nu se apeleaza pe ea insasi (nu contine auto-apeluri)
    #procedura afiseaza toate secventele de n paranteze corect construite
    #date de intrare: n - intreg (lungimea unei secvente de paranteze = numarul de paranteze care va fi generat)
    #date de iesire: -

    sol = [-1]  #candidate solution
    while len(sol) > 0:
        ales = False #variabila booleana de tip semafor care va marca daca s-a gasit sau nu o componenta valida pentru solutia candidat curenta
                     #cu alte cuvinte, variabila ales va semnala daca se poate continua procesul generativ sau daca trebuie sa se faca revenirea la un pas anterior (semn ca solutia candidat curenta nu poate sa fie solutie (fezabila))
        while not ales and len(sol) <= n and sol[-1] < 1:
            sol[-1] += 1  #increase the last component
            ales = ebun(sol, len(sol) - 1) #validam componenta curenta (verificam daca ea este sau nu valida)
        if ales: #s-a gasit o componenta buna (se va pastra aceasta componenta si se va continua procesul de generare a unei noi componente)
            if esol(sol, len(sol), n):
                #avem solutie (fezabila)
                print_solution(sol) #afisam solutia gasita (generata)
            sol.append(-1)  #expand candidate solution
        else: #nu s-a gasit o componenta valida (care sa conduca la o solutie)
            sol = sol[:-1]  #go back one component
                            #sol[:-1] face o copie shallow (se copiaza prin valoare, ci nu prin referinta) a listei sol fara ultimul element (cel de pe pozitia len(sol) - 1)

def pb7():
    print('Enunț problema 7:\nPentru un n dat generați toate secvențele de paranteze care se închid corect.\nExamplu: n=4\ndouă soluții: (()) și ()()', end = '\n\n')
    try:
        n = int(input('n = ')) #citim numarul parantezelor pe care dorim sa le generam (lungimea unei secvente de paranteze)
    except ValueError as ve:
        print(ve)
        return
    except TypeError as te:
        print(te)
        return
    except Exception as ex:
        print(ex)
        return
    assert(n >= 0) #numarul parantezelor dintr-o secventa trebuie sa fie un numar intreg fara semn (unsigned), adica un numar natural (intreg pozitiv)
    if n % 2: #if n % 2 == 1:
        #o secventa de paranteze este corect construita daca (conditie necasara, dar nu suficienta):
        #numarul parantezelor deschise este egal cu numarul parantezelor inchise (*)
        #fie k0 - numarul parantezelor deschise din secventa
        #    k1 - numarul parantezelor inchise din secventa
        #avem urmatoarea relatie: k0 + k1 = n (suma dintre numarul parantezelor deschise si cel al parantezelor inchise ne da numarul total de paranteze din secventa)
        #din (*) => k0 = k1 = k => k + k = n => 2k = n => n este numar par (de forma 2k, cu k - numar natural)
        print('Nu exista secvente corect parantezate de lungime impara!') #afisam mesaj corespunzator pe ecran (in consola/terminal)
        return
    print('\nSecventele de', n, 'paranteze care se inchid corect sunt:')
    sol = [None] * n #rezervam n elemente (de la 0 la n - 1) pentru vectorul (sirul) solutie sol in care vom memora componentele generate (adica solutiile candidat)
    sol[0] = 0     #orice secventa corect parantezata incepe cu o paranteza deschisa (0)
    sol[n - 1] = 1 #orice secventa corect parantezata se termina cu o paranteza inchisa (1)
    #folosind paradigma de programare (paradigma algoritmica) backtracking vom genera doar n - 2 paranteze (pentru ca prima si ultima paranteza sunt fixate)
    #astfel, o solutie (fezabila) va fi de forma:
    #0, ..., 1; unde 0 - paranteza deschisa
    #                1 - paranteza inchisa
    print('\nI - varianta recursiva:')
    recursive_backtracking(sol, 1) #apelam varianta recursiva/recurenta de backtracking
    global nr_sol #facem vizibila variabila globala nr_sol in functia main
    nr_sol = 0 #resetam contorul de solutii
    print('\nII - varianta iterativa:')
    iterative_backtracking(n) #apelam varianta iterativa (fara auto-apeluri) de backtracking

pb7() #apelul functiei procedurale (procedurii) pb7 (programul principal)
