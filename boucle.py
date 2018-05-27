#### boucle while ####
nb = 7
i = 0

while i < 10:
    print(nb," fois",i,"=",i * nb)
    i += 1

# boucle for
chaine = "bonjour les copains"
for lettre in chaine:
    print(lettre)

#voyelle
for lettre in chaine:
    if lettre in "aeiouy":
        print(lettre)
    else:
        print('*')