import os
import traceback

# [Ficha 04 - Ex. 05] - Imprime o primeiro e último nome de um nome completo

try:
    while True:
        try:
            frase = str(input("Nome: "))
            if frase.replace(" ", ""):
                if frase.count(" ") >= 1: break
        except:
            continue
    print(frase.split(" ")[0] + " " + frase.split(" ")[-1])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
