#8. Generați toate sub-secvențele de lungime 2n+1, formate din 0, -1 și 1, astfel încât
#a1 = 0, ..., a2n+1 = 0 și |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n.

#variabile globale in care contorizam solutiile fezabile (gasite/descoperite) pentru fiecare dintre cele
#doua variante ale functiei Backtracking (atat cea iterativa cat si cea recursiva/recurenta)
#nr_sol_rec  - numar solutii varianta recursiva
#nr_sol_iter - numar solutii varianta iterativa
nr_sol_rec = nr_sol_iter = 0 #nr_sol_rec, nr_sol_iter = 0, 0

def ebun(n, a):
    #functie operand (rezultat) care returneaza (furnizeaza) o valoare logica (booleana), ci anume True daca ultima componenta generata este valida si False in caz contrar
    #aceasta este functia care verifica (valideaza) consistenta solutiei candidad prin validarea ultimei componente adaugate la aceasta (adica in lista a)
    #cu alte cuvinte, daca ultima componenta generata si adaugata la solutia candidat a curenta este valida, atunci prin extinderea solutiei curente (prin generarea de noi componente) se poate obtine o solutie (fezabila)
    #in caz contrar, ultima componenta altereaza proprietatea de corectitudine a solutiei candidat (cu alte cuvinte, din solutia candidat curenta nu se va putea obtine o solutie fezabila)
    #date de intrare: a - lista de intregi (din multimea {-1, 0, 1}) care reprezinta solutia candidat curenta
    #                 n - numar intreg cu proprietatea ca 2 * n + 1 reprezinta numarul de elemente/componente pe care trebuie sa il contina o solutie (fezabila)
    #date de iesire: False - daca ultima componenta generata (a[-1]) nu este valida (aceasta va fi inlocuita cu o alta valoare din domeniul componentelor {-1, 0, 1} in functia de backtracking)
    #                True  - daca ultima componenta adaugata la solutia candidat a este valida (aceasta se va pastra si se va continua algoritmul cu generarea de noi componente pentru vectorul solutie)

    #ternary operator:
    #[on_true] if [expression] else [on_false]
    return False if (len(a) == 1 or len(a) == 2 * n + 1) and a[-1] else (True if len(a) == 1 else a[-1] != a[-2])

    '''
    if (len(a) == 1 or len(a) == 2 * n + 1) and a[-1]: #prima si ultima componenta din solutie trebuie sa fie 0 (adica in solutia candidat a trebuie sa avem 0 pe prima pozitie (0) si pe ultima (2 * n))
                                                       #conditie (de corectitudine) necesare dar nu suficienta
        return False #daca primul element sau ultimul din lista a sunt nenule (diferite de 0), atunci solutia candidat nu este o solutie (fezabila)
    return True if len(a) == 1 else a[-1] != a[-2] #de asemenea, intr-o solutie fiecare doua componente adiacente/vecine trebuie sa fie diferite/distincte ca si valoare
    '''

def esol(n, a):
    #functie operand care returneaza o valoare booleana (False sau True)
    #aceasta este functia solution care verifica daca s-au generat 2 * n + 1 componente pentru solutia candidat a (caz in care solutia este fezabila)
    #cu alte cuvinte, daca lungimea (numarul de elemente al) listei a este egala cu 2 * n + 1
    #aceasta functie verifica daca o solutie candidat (a) este sau nu solutie (fezabila)
    #date de intrare: n - numar intreg fara semn (unsigned), adica un numar natural
    #                 a - lista de numere intregi (solutia candidat)
    #date de iesire: False - solutia candidat a nu este fezabila
    #                True  - solutie candidat a este solutie (fezabila)

    #pentru ca o solutie candidat sa fie fezabila aceasta trebuie sa aiba lungime 2 * n + 1
    return len(a) == 2 * n + 1 #return True if len(a) == 2 * n + 1 else False

def afisare_solutie(a, varianta = 'recursiva'):
    #procedura (functie procedurala, de tip void = vid) care afiseaza o solutie (fezabila) pe ecran (in consola/terminal)
    #valoarea variabilei tablou (unidimensional de caractere = sir de caractere) varianta poate sa fie 'recursiva' sau 'iterativa' daca se precizeaza
    #date de intrare: a        - lista de numere intregi din intervalul [-1, 1] care reprezinta o solutie (fezabila)
    #                 varianta - parametru/argument optional (by default = implicit/prestabilit acesta are ca si valoare sirul de caractere 'recursiva') de tip string care reprezinta metoda de backtracking pentru care se face tiparirea solutie
    #date de iesire: -

    assert varianta == 'recursiva' or varianta == 'iterativa'
    if varianta == 'recursiva': #varianta recursiva
        global nr_sol_rec #facem vizibila variabila globala nr_sol_rec in functia curenta pentru a ii putea modifica/altera continutul
        nr_sol_rec += 1 #contorizam numarul solutiilor (fezabile) gasite pentru varianta recursiva prin incrementarea variabilei nr_sol_rec cu 1
        #afisam mesaj varianta recursiva/recurenta
        print('Solutia (varianta recursiva) #', end = '')
        print(nr_sol_rec, end = ': [')
    else: #varianta iterativa
        global nr_sol_iter #facem vizibila variabila globala nr_sol_iter in functie pentru a o putea modifica
        nr_sol_iter += 1 #contorizam numarul solutiilor (fezabile) gasite pentru varianta iterativa prin incrementarea cu 1 a variabilei nr_sol_iter
        #afisam mesaj varianta iterativa (non-recursiva)
        print('Solutia (varianta iterativa) #', end = '')
        print(nr_sol_iter, end = ': [')
    for component in a[:-1]: #parcurgem vectorul solutie de la prima (a[0]) pana la penultima componenta (a[-2] == a[len(a) - 2])
        print(component, end = ', ') #afisam componenta curenta (component) din solutie urmata de caracterul , si spatiu pentru delimitarea componentelor solutiei
    print(a[-1], end = ']\n') #tiparim ultima componenta (a (2 * n + 1)-a din solutie, adica componenta a[-1] == a[len(a) - 1]) urmata de caracterul '\n' care simuleaza trecerea la rand nou (linie noua)

def recursive_backtracking(n, a = []):
    #procedura de backtracking recursiv/recurent care genereaza secvente de 2 * n + 1 componente din multimea {-1, 0, 1} cu proprietatea ca o secventa incepe si se termina cu 0 si nu poate contine elemente egale pe pozitii consecutive
    #date de intrare: n - int
    #                 a - lista de int-uri (solutia candidat), acest parametru/argument este unul optional (daca nu se specifica la apel atunci lista a va fi initializata ca fiind o lista vida)
    #date de iesire: -

    for component in [-1, 0, 1]: #for component in range(-1, 2):
                                 #parcurgem domeniul de definitie al unei componente ce poate alcatui o solutie in cadrul problemei
        a.append(component) #adaugam componenta component la solutia candidat curenta (adica in lista a pe ultima pozitie)
        if ebun(n, a): #daca componenta nou adaugata (adica component) este valida atunci se va pastra
            if esol(n, a): #verificam daca solutia candidat a este sau nu solutie (fezabila)
                #solutia candidat a este fezabila (contine 2 * n + 1 componente/elemente)
                #afisam solutia gasita
                afisare_solutie(a) #afisare_solutie(a, varianta = 'recursiva')
            else: #elif len(a) < 2 * n + 1:
                #solutia candidat nu este fezabila (nu s-au generat 2 * n + 1 componente pentru aceasta)
                recursive_backtracking(n, a) #apelam functia recursive_backtracking pentru acelasi n si noua lista a (cu componenta component pe ultima pozitie)
        a.pop() #facem backtrack (revenim la pasul anterior/precedent) datorita faptului ca nu s-au mai gasit componente valide penttu solutia candidat curenta (s-a epuizat intreg spatiul de cautare pentru o noua componenta)
                #a.pop() - stergem ultima componenta din lista (eliminam ultima componenta)

def iterative_backtracking(n):
    #functie procedurala de backtracking iterativ care genereaza secvente de 2 * n + 1 componente din multimea {-1, 0, 1} cu proprietatea ca o secventa incepe si se termina cu 0 si nu poate contine elemente egale pe pozitii consecutive
    #date de intrare: n - int
    #date de iesire: -

    a = [-2] #candidate solution
             #solutia candidat curenta
    while len(a): #while len(a) > 0:
                  #while len(a) != 0:
                  #lista a nu este vida (este nevida <=> se mai pot genera componente pentru aceasta)
        ales = False #variabila semafor (booleana) care ne indica (semnaleaza) daca s-a gasit o componenta valida pentru solutia candidat curenta
                     #ales reprezinta un flag (un indicator pe un singur bit)
        while not ales and len(a) <= 2 * n + 1 and a[-1] < 1: #bucla (instructiune repetitiva/ciclica) in care cautam o componenta valida pentru solutia candidat curenta
            a[-1] += 1 #a[len(a) - 1] += 1
                       #increase the last component
                       #incrementam continutul ultimei componente din solutia candidat (adica a celei mai recente componente generate)
                       #astfel, pentru o componenta, vom parcurge (epuiza) intreg domeniul acesteia (in cazul nostru multimea {-1, 0, 1})
            ales = ebun(n, a) #verificam daca a[-1] este o componenta valida sau nu (validam componenta de pe pozitia -1 din lista a (adica componenta a[-1]))
        if not ales: #nu s-a gasit o solutie valida pentru solutia candidat curenta (s-a epuizat intreg domeniul componentelor)
            a = a[:-1] #a.pop()
                       #go back one component
                       #a[:-1] - face o copie shallow (se copiaza prin valoare ci nu prin referinta) a listei a fara ultimul element (a[-1], cel de pe pozitia -1 == len(a) - 1 din lista a)
                       #daca nu se mai pot genera solutii pentru solutia candidat a atunci se va face backtrack (adica se va reveni la componenta anterioara/precedenta)
        else: #s-a descoperit o componenta valida pentru solutia candidat
            if esol(n, a): #daca solutia candidat a este fezabila atunci aceasta se va afisa in consola/terminal (adica pe ecran la iesirea standard)
                afisare_solutie(a, varianta = 'iterativa') #printam la iesirea standard (stdout = standard output) solutia gasita (generata)
            a.append(-2) #expand candidate solution
                         #expandam solutia candidat (generam noi componente pentru aceasta)

def pb8():
    #0, ..., -1, -1, ..., 0 - NU (|(-1) - (-1)| = |-1 - (-1)| = |-1 + 1| = |0| = 0)
    #0, ..., -1,  0, ..., 0 - DA (|0 - (-1)| = |0 + 1| = |1| = 1)
    #0, ..., -1,  1, ..., 0 - DA (|1 - (-1)| = |1 + 1| = |2| = 2)

    #0, ...,  0, -1, ..., 0 - DA (|(-1) - 0| = |-1 - 0| = |-1| = 1)
    #0, ...,  0,  0, ..., 0 - NU (|0 - 0| = |0| = 0)
    #0, ...,  0,  1, ..., 0 - DA (|1 - 0| = |1| = 1)

    #0, ...,  1, -1, ..., 0 - DA (|(-1) - 1| = |-1 - 1| = |-2| = 2)
    #0, ...,  1,  0, ..., 0 - DA (|0 - 1| = |-1| = 1)
    #0, ...,  1,  1, ..., 0 - NU (|1 - 1| = |0| = 0)

    #Conditie de corectitudine a unei secvente:
    #nu avem voie sa avem -1 urmat de -1
    #nu avem voie sa avem 0 urmat de 0
    #nu avem voie sa avem 1 urmat de 1
    #=> nu avem voie sa avem doua elemente egale pe pozitii consecutive (succesive)

    #Asadar, trebuie ca:
    #1. a1 = a2n+1 = 0
    #2. |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n
    #   |a(i+1) - ai| != 0     , pentru orice i, 1 <= i <= 2n
    #   a(i+1) - ai != 0       , pentru orice i, 1 <= i <= 2n
    #   a(i+1) != ai           , pentru orice i, 1 <= i <= 2n

    print('Enunț problema 8:\nGenerați toate sub-secvențele de lungime 2n+1, formate din 0, -1 și 1, astfel încât a1 = 0, ..., a2n+1 = 0 și |a(i+1) - ai| = 1 sau 2, pentru orice i, 1 <= i <= 2n.\n')
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
    print('\nSolutii varianta recursiva:')
    recursive_backtracking(n)
    global nr_sol_rec
    if not nr_sol_rec:
        print('Nu exista solutie pentru varianta recursiva!')
    print('\nSolutii varianta iterativa:')
    iterative_backtracking(n)
    global nr_sol_iter
    if not nr_sol_iter:
        print('Nu exista solutie pentru varianta iterativa!')
    assert nr_sol_rec == nr_sol_iter

pb8()