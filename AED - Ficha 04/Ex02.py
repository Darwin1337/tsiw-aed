import os
import traceback

# [Ficha 04 - Ex. 02] - Imprime o número de espaços, de caracteres e de vogais de uma string

try:
    vogais = ["a", "e", "i", "o", "u"]
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    print("Número de caracteres: " + str(len(frase.replace(" ", ""))))
    print("Número de vogais: " + str(sum(letra in vogais for letra in frase)))
    print("Número de espaços: " + str(frase.count(" ")))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
