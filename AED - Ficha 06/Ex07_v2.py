import os
import traceback
import random

# [Ficha 06 - Ex. 07] - Ordena uma lista de valores de forma decrescente e imprime os valores e os seus respetivos meses

# BUG: Se houver dois ou mais valores iguais o programa pode falhar

def ordenarLista(a):
    a = sorted(a, reverse=True)
    for x in range(len(a)):
        print(str(a[x]) + " - " + meses[valores.index(a[x])])

try:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    valores = [random.randint(1, 500) for x in range(len(meses))]
    print("\nOriginal:\n")
    for x in range(len(meses)):
        print(str(valores[x]) + " - " + meses[x])
    print("\nOrdenada:\n")
    ordenarLista(valores)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
