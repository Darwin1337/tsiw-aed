import os
import traceback

# [Ficha 01 - Ex. 03] - Calcula o peso ideal dada a altura e o género da pessoa

try:
    isOptionCorrect, isNumberCorrect = False, False
    while not isOptionCorrect:
        os.system('cls' if os.name=='nt' else 'clear')
        print("[1] - Feminino\n[2] - Masculino")
        try:
            opcao = int(input("\nOpção: "))
            if opcao == 1 or opcao == 2:
                isOptionCorrect = True
        except:
            continue
    while not isNumberCorrect:
        try:
            num = int(input("\nIntroduza a altura em centímetros: "))
            if int(num) >= 120 and int(num) <= 220:
                isNumberCorrect = True
        except:
            continue
    print("\nPeso ideal: " + str(float((num - 100) * 0.85)) + "kg") if opcao == 1 else print("\nPeso ideal: " + str(float((num - 100) * 0.90)) + "kg")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
