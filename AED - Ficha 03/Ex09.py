import os
import traceback

# [Ficha 03 - Ex. 09] - Verifica se um número é perfeito

try:
    soma = 0
    while True:
        try:
            num = int(input("Introduza um número: "))
            if num > 0: break
        except:
            continue
    for x in range(num - 1, 0, -1):
        if num % x == 0:
            soma += x
    print("É perfeito") if soma == num else print("Não é perfeito")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
