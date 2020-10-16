import os
import traceback

# [Ficha 01 - Ex. 04] - Calcula o IMC dado o peso e a altura da pessoa

try:
    isNumberCorrect1, isNumberCorrect2 = False, False
    while not isNumberCorrect1:
        try:
            altura = float(str(input("Introduza a altura em metros: ")).replace(",", "."))
            if altura >= 1.20 and altura <= 2.20:
                isNumberCorrect1 = True
        except:
            continue
    while not isNumberCorrect2:
        try:
            peso = float(str(input("Introduza o peso em kilogramas: ")).replace(",", "."))
            if peso >= 35 and peso <= 350:
                isNumberCorrect2 = True
        except:
            continue
    print("\nIMC: %.2f" %float(peso / (altura*altura)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
