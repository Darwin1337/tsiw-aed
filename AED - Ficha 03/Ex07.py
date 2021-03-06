import os
import traceback

# [Ficha 03 - Ex. 07] - Verifica se um número é primo ou não

try:
    isDivisible = False
    while True:
        try:
            num = int(input("Introduza um número: "))
            if num > 0: break
        except:
            continue
    for x in range(num - 1, 1, -1):
        if num % x == 0:
            isDivisible = True
            break
    print("É primo") if not isDivisible else print("Não é primo")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
