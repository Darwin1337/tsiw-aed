import os
import traceback

# [Ficha 06 - Ex. 01] - Recebe uma lista com 10 números inteiros e devolve quantos desses números estão acima da média

def acimaMedia():
    numeros, result = [], ""
    for x in range(10):
        while True:
            try:
                num = int(input("Introduza o número " + str(x + 1) + ": "))
                if num >= 0:
                    numeros.append(num)
                    break
            except:
                continue
    media = float(sum(numeros) / len(numeros))
    result += "\nMédia: " + str(media)
    result +=  "\nQuantidade de números acima da média: " + str(sum(float(num) > media for num in numeros))
    return result

try:
    print(str(acimaMedia()))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
