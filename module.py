import math # import du module math
print(math.sqrt(16)) # fonction racine carre

help(math)

import math as mathematiques # definition du namespace
print(mathematiques.sqrt(25))

from math import fabs # import d'une fonction uniquement
print(fabs(-5))
print(fabs(2))

from math import * # import de toute les fonctions dans le namespace
## warning linting 
print(sqrt(4))
print(fabs(5))
