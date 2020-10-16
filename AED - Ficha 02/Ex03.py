import os
import traceback

# [Ficha 02 - Ex. 03] - Calcula o peso ideal dado o género e a altura da pessoa

try:
    isOptionCorrect, isNumberCorrect = False, False
    while not isOptionCorrect:
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            opcao = str(input("Género (M = Masculino | F = Feminino): "))
            if opcao.lower() == "m" or opcao.lower() == "f":
                isOptionCorrect = True
        except:
            continue
    while not isNumberCorrect:
        try:
            altura = float(str(input("Introduza a altura em metros: ")).replace(",", "."))
            if altura >= 1.20 and altura <= 2.20:
                isNumberCorrect = True
        except:
            continue
    print("\nPeso ideal: " + str(float((((altura * 100) - 100) - ((altura * 100) - 150) / 4))) + "kg") if opcao.lower() == "m" else print("\nPeso ideal: " + str(float((((altura * 100) - 100) - ((altura * 100) - 150) / 4))) + "kg")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
