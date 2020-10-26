import os
import traceback

# [Ficha 04 - Ex. 07] - Determina a posição e a ocorrência de uma determinada palavra num texto

try:
    countOcorrencias, posTemp, posicoesEncontradas = 0, 0, ""
    while True:
        try:
            texto = str(input("Texto: "))
            if texto.replace(" ", ""):
                texto = texto.lower()
                break
        except:
            continue
    while True:
        try:
            palavra = str(input("\nPalavra a procurar: "))
            if palavra.replace(" ", ""):
                palavra = palavra.lower()
                break
        except:
            continue
    for x in range(texto.count(palavra)):
        posicoesEncontradas += str(texto.find(palavra, posTemp, len(texto)) + 1) + ", "
        posTemp = int(posicoesEncontradas.replace(", ", "").split(", ")[-1]) + len(palavra)
    print("\nN.º de ocorrências: " + str(texto.count(palavra)) + "\nPosições: " + posicoesEncontradas[:-2]) if posicoesEncontradas else print("\nSem correspondências")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
