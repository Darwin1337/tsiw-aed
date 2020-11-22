import os
import traceback

# [Ficha 05 - Ex. 02] - Função que devolve o número de palavras, contidas numa string e
#                       que ocorrem mais do que uma vez.

def numPalavras(frase):
    allowedChars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    inputArray = frase.split(" ")
    outputArray = []
    palavrasIguais = []
    for x in range(len(inputArray)):
        isInList = False
        inLoop = ''.join(filter(allowedChars.__contains__, inputArray[x]))
        for j in range(len(outputArray)):
            if inLoop.lower() == outputArray[j].lower():
                isInList = True
                palavrasIguais.append(inLoop)
                break
        if not isInList: outputArray.append(inLoop)
    return len(set(palavrasIguais))

try:
    while True:
        try:
            frase = str(input("Frase: "))
            if frase.replace(" ", ""): break
        except:
            continue
    print("N.º de palavras que ocorrem mais que uma vez: " + str(numPalavras(frase)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
