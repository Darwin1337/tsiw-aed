import os
import traceback

# [Ficha 05 - Ex. 01] - Determina o fatorial de um número

def fatorial(numero):
    for x in range(numero - 1, 0, -1):
        numero *= int(x)
    return numero

try:
    while True:
        try:
            num = int(input("Introduza um número: "))
            if num >= 0: break
        except:
            continue
    print("Fatorial: " + str(fatorial(num))) if num > 0 else print("Fatorial: 1")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
