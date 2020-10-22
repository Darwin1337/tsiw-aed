import os
import traceback

# [Ficha 04 - Ex. 02] - Imprime o número de espaços, de caracteres e de vogais de uma string

try:
    result, countVogais, countSpaces = "", 0, 0
    vogais = ["a", "e", "i", "o", "u"]
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    for x in range(len(frase)):
        if frase[x] in vogais:
            countVogais += 1
    for x in range(len(frase)):
        if frase[x] == " ":
            countSpaces += 1
    print("Número de caracteres: " + str(len(frase.replace(" ", ""))))
    print("Número de vogais: " + str(countVogais))
    print("Número de espaços: " + str(countSpaces))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
