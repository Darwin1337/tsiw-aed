import os
import traceback

# [Ficha 04 - Ex. 04] - Elimina dois ou mais espaços seguidos de uma string

try:
    result, countSpaces = "", 0
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    for x in range(len(frase.strip().split(" "))):
        if frase.strip().split(" ")[x]: result += frase.strip().split(" ")[x] + " "
    print(result.strip())
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
