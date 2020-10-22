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
    for x in range(len(frase)):
        if frase[x] == " ": countSpaces += 1
        else: countSpaces = 0
        if countSpaces <= 1: result += frase[x]
    print(result)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
