import os
import traceback

# [Ficha 02 - Ex. 02] - Classifica um triângulo quanto aos lados

try:
    ladosTriangulo, iguais = [], 0
    for x in range(3):
        isNumberCorrect = False
        while not isNumberCorrect:
            try:
                temp = int(input("Introduza o tamanho do lado " + str(x + 1) + ": "))
                if int(temp) > 0:
                    ladosTriangulo.append(temp)
                    isNumberCorrect = True
            except:
                continue
    mensagens = ["O triângulo é equilátero - lados todos iguais.", "O triângulo é isósceles - dois lados iguais.", "O triângulo é escaleno - lados todos diferentes."]
    print(mensagens[len(set(ladosTriangulo)) - 1])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
