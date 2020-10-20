import os
import random
import traceback

# [Ficha 03 - Ex. 06] - Verifica se um ano (gerado aleatoriamente) é bissexto ou não

try:
    ano = random.randint(1900, 2020)
    print("Ano gerado: " + str(ano))
    print("O ano " + str(ano) + " é bissexto") if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else print("O ano " + str(ano) + " não é bissexto")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
