import os
import traceback

# [Ficha 04 - Ex. 09] - Substitui algarismos num texto pela sua forma extensa

try:
    result = ""
    algarismos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    extenso = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    while True:
        try:
            texto = str(input("Texto: "))
            if texto.replace(" ", ""): break
        except:
            continue
    for x in range(len(texto)):
        foundDigit = False
        for j in range(len(algarismos)):
            if texto[x] == str(algarismos[j]):
                foundDigit = True
                result += extenso[j]
        if not foundDigit: result += texto[x]
    print(result)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
