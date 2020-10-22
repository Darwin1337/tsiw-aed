import os
import traceback

# [Ficha 04 - Ex. 06] - Normaliza nomes próprios, por ex: “Carlos Alberto Costa Pereira” > “Carlos A. C. Pereira”

try:
    result = ""
    while True:
        try:
            frase = str(input("Nome: "))
            if frase.replace(" ", ""): break
        except:
            continue
    resultado = frase.split(" ")[0] + " "
    for x in range(1, len(frase.split(" ")) - 1, 1):
        resultado += frase.split(" ")[x][0:1].upper() + ". "
    print(resultado + frase.split(" ")[len(frase.split(" ")) - 1])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
