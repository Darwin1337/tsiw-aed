import os
import traceback
import random

# [Ficha 06 - Ex. 07] - Ordena uma lista de valores de forma decrescente

def ordenarLista(a):
    return sorted(a, reverse=True)

try:
    valores = [random.randint(1, 500) for x in range(12)]
    print(str(valores) + "\n")
    print(str(ordenarLista(valores)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
