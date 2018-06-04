# fonction sans parametres
def table_par_7():
    nb = 7
    i = 0
    while i < 10:
        print(i +1 ,"*",nb,"=",(i +1) * nb)
        i += 1
table_par_7()
#fonction avec paramètres
def table(nb):
    i = 0
    while i < 10:
        print(i +1 ,"*",nb,"=",(i +1) * nb)
        i += 1
table(50)
#fonction avec 2 paramètres
def table2(nb,max):
    i = 0
    while i < max:
        print(i +1 ,"*",nb,"=",(i +1) * nb)
        i += 1
table2(3,15)
#fonction avec 2 paramètres et un defaut
def table10(nb, max=10):
    i = 0
    while i < max:
        print(i +1 ,"*",nb,"=",(i +1) * nb)
        i += 1
table10(5)
#fonction avec docstring (help)
def testhelp(nb,max=10):
    """test de fonction affichant la table de multiplication par nb 
    par defaut max = 10"""
    i = 0
    while i < max:
        print(i +1 ,"*",nb,"=",(i +1) * nb)
        i += 1
# help(testhelp) # affiche le docstring
#test2

def carre(valeur):
    return valeur * valeur

mavariable = carre(6)
print(mavariable)

f = lambda x: x * x
print(f(25))
print(f(-5))

f = lambda x,y: x+y
print(f(1,2)) 

