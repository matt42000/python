# fonction input
year = input("saisie de l'année: ")
print(year)
print(type(year))
#conversion string to int
year = int(year)
print(year)
print(type(year))
bisextile = False

if year % 400 == 0:
    bisextile = True
elif year % 100 == 0:
    bisextile = False
elif year % 4 == 0:
    bisextile = True
else:
    bisextile = False

if bisextile:
    print("l'année est bisextile")
else:
    print("l'année n'est pas bisextile")
