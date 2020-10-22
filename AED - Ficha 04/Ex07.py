import os
import traceback

# [Ficha 04 - Ex. 07] - Determina a posição e a ocorrência de uma determinada palavra num texto

try:
    pos, counter, iterator = "", 0, 0
    while True:
        try:
            texto = str(input("Texto: "))
            if texto.replace(" ", ""): break
        except:
            continue
    while True:
        try:
            palavra = str(input("\nPalavra a procurar: "))
            if palavra.replace(" ", ""): break
        except:
            continue
    while iterator <= len(texto) - 1:
        if texto[iterator].lower() == palavra[0].lower():
            if len(texto) - (iterator + 1) >= len(palavra) - 1:
                notTheSame = False
                for j in range(1, len(palavra)):
                    if texto[iterator + j].lower() != palavra[j].lower():
                        notTheSame = True
                        break
                if not notTheSame:
                    counter += 1
                    pos += str(iterator + 1) + ", "
                    iterator += len(palavra) - 1
            else: break
        iterator += 1
    if counter == 0: pos = "Nenhuma  "
    print("\nN.º de ocorrências: " + str(counter))
    print("Posição: " + pos[:-2])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
