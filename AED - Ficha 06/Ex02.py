import os
import traceback
import random

# [Ficha 06 - Ex. 02] - Gera uma chave aleatória do Euromilhões [5 números inteiros entre 1 e 50, e duas estrelas entre 1 e 12]
# Atenção: Não pode ter números repetidos nem estrelas repetidas

# FALTA: Perguntar ao utilizador se quer gerar outra chave

def gerarChave():
    numeros, estrelas, result = [], [], "Números: "
    for i in range(5):
        while True:
            rand = random.randint(1, 50)
            if rand not in numeros:
                numeros.append(rand)
                break
    for i in range(2):
        while True:
            rand = random.randint(1, 12)
            if rand not in estrelas:
                estrelas.append(rand)
                break
    for num in numeros:
        result += str(num) + " "
    result += "Estrelas: "
    for num in estrelas:
        result += str(num) + " "
    return result

try:
    print("Chave gerada:\n" + str(gerarChave()))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
