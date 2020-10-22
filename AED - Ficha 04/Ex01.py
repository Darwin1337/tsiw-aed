import os
import traceback

# [Ficha 04 - Ex. 01] - Inverte uma string

try:
    result = ""
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    for x in range(len(frase) - 1, -1, -1):
        result += frase[x]
    print(result)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
