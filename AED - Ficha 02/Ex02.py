import os
import traceback

# [Ficha 02 - Ex. 02] - Classifica um triângulo quanto as lados

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
    for x in range(len(ladosTriangulo)):
        for j in range(len(ladosTriangulo)):
            if ladosTriangulo.count(ladosTriangulo[0]) < len(ladosTriangulo):
                if int(x) != int(j) and int(ladosTriangulo[x]) == int(ladosTriangulo[j]):
                    iguais += 1
            else:
                iguais = 3
                break
    mensagens = ["O triângulo é escaleno - lados todos diferentes.", "O triângulo é isósceles - dois lados iguais.", "O triângulo é equilátero - lados todos iguais."]
    print("\n" + mensagens[iguais - 1]) if iguais != 0 else print("\n" + mensagens[0])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
