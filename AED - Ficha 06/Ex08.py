import os
import traceback
import random

# [Ficha 06 - Ex. 08] - Ordena a lista e permite gerar uma outra sem valores duplicados

def ordenarLista(a):
    a = sorted(a)
    print("\nLista ordenada: " + str(a))
    while True:
        try:
            opcao = str(input("\nPretende criar outra lista sem duplicados (S/N): "))
            if opcao.replace(" ", ""):
                if opcao.lower() == "s":
                    print("\nLista sem duplicados: " + str(list(set(sorted(a)))))
                    break
                elif opcao.lower() == "n":
                    break
        except: continue

try:
    while True:
        try:
            num = int(input("Tamanho da lista: "))
            if num > 1: break
        except: continue
    lista = [random.randint(1, 20) for x in range(num)]
    ordenarLista(lista)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
