import os
import traceback

# [Ficha 05 - Ex. 04] - Implementa a cifra de César

def cifraCesar(a, b):
    result = ""
    for i in range(len(a)):
        if int(ord(a[i])) + chave > 255: result += chr(((int(ord(a[i])) + chave) - 255) - 1)
        else: result += chr(int(ord(a[i])) + chave)
    return result

try:
    while True:
        try:
            frase = str(input("Texto: "))
            if frase.replace(" ", ""): break
        except:
            continue
    while True:
        try:
            chave = int(input("Chave: "))
            if chave >= 1 and chave <= 20: break
        except:
            continue
    print("\nTexto Criptografado: " + str(cifraCesar(frase, chave)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
