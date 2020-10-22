import os
import traceback
import time

# [Ficha 04 - Ex. 04] - Elimina dois ou mais espaços seguidos de uma string

try:
    result, countSpaces = "", 0
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    for x in range(len(frase.split(" "))):
        if frase.split(" ")[x]: result += frase.split(" ")[x] + " "
    print(result.strip())
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
