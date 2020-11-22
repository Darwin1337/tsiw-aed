import os
import traceback
import random

# [Ficha 06 - Ex. 09] - Dá merge a duas listas mantendo a ordenção

def mergeLista(a, b):
    return sorted(lista1 + lista2)

try:
    lista1 = [x + 1 for x in range(1, 21, 2)]
    lista2 = [x + 1 for x in range(2, 21, 2)]
    print(str(lista1) + "\n" + str(lista2) + "\n" + str(mergeLista(lista1, lista2)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
