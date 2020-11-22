import os
import traceback
import random

# [Ficha 06 - Ex. 06v1] - Lê uma lista de 10 números inteiros e indica se um determinado valor pesquisado
# existe na lista - em caso afirmativo determinar a sua posição (primeira ocorrência)

def pesquisaLista(a):
    if a in valores:
        for x in range(len(valores)):
            if a == valores[x]:
                print("O valor foi encontrado na posição " + str(x + 1))
                break
    else:
        print("O valor pesquisado não foi encontrado")

try:
    valores = [random.randint(1, 100) for x in range(10)]
    print("Lista gerada = " + str(valores))
    while True:
        try:
            num = int(input("Pesquisar pelo número: "))
            if num >= 1 and num <= 100: break
        except:
            continue
    pesquisaLista(num)
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
