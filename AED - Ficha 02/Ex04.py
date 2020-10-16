import os
import traceback

# [Ficha 02 - Ex. 04] - Apresenta a classificação de acordo com o IMC (obtido através do peso e da altura da pessoa)

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
    mensagens = ["0-18.5;Abaixo do Peso", "18.6-24.9;Saudável", "25-29.9;Sobrepeso", "30-34.9;Obesidade Grau I", "35-39.9;Obesidade Grau II (severa)", "40-75;Obesidade Grau III (mórbida)"]
    for x in range(len(mensagens)):
        if float(peso / (altura*altura)) >= float(mensagens[x].split(";")[0].split("-")[0]) and float(peso / (altura*altura)) <= float(mensagens[x].split(";")[0].split("-")[1]):
            print("\nResultado: " + str(mensagens[x].split(";")[1]))
            break
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
