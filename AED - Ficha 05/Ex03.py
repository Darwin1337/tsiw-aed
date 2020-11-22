import os
import traceback

# [Ficha 05 - Ex. 03] - Devolve a média aritmética dos números recebidos

def mediaAritmetica(total):
    soma = 0.0
    for x in range(total):
        while True:
            try:
                numero = int(input("Introduza o número " + str(x + 1) + ": "))
                if numero >= 0:
                    soma += numero
                    break
            except:
                continue
    return float(soma/total)

try:
    while True:
        try:
            num = int(input("Quantidade de números: "))
            if num > 0: break
        except:
            continue
    print("Média Aritmética: " + str(mediaAritmetica(num)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
