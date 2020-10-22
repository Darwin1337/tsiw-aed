import os
import traceback

# [Ficha 04 - Ex. 03] - Lê um texto e verifica se é capicua ou não

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
    print("É capicua") if result == frase else print("Não é capicua")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
