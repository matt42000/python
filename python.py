print("hello")
a = 0
print(a)
mavariabledeouf = "salut les copains"
print(mavariabledeouf)
mavariable2 = 6
# boucle if
if a > 0: # attention au ":"
    print("a est supérieur à Zero") # tab obligatoire
if a < 0:
    print("a est inférieur à zéro")
if a > 0:
    print("a est positif")
else:
    print("a est négatif")
#elif
if a > 0: # Positif
    print("a est positif.")
elif a < 0: # Négatif
    print("a est négatif.")
else: # Nul
    print("a est nul.")

# boolean
boule = 1 #affectation
print(type(boule))
boule == 0 # comparaison ( false )
boule != 10 
print(type (boule > 0)) 

# or and
b = 4
if b>=2 and b<=8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")
if b<2 or b>8:
    print("a n'est pas dans l'intervalle.")
else:
    print("a est dans l'intervalle.")

#
majeur = False
if majeur is not True:
    print("pas majeur")
else:
    print("majeur")