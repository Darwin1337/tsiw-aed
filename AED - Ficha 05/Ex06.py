import os
import traceback

# [Ficha 05 - Ex. 06] - Recebe um número entre 1 e 999 e devolve o mesmo valor em numeração Romana
# I	Corresponde ao numeral 1.
#       II são dois, III são três, IV são 4
# V	Corresponde ao numeral 5.
#       IV são 4, VI são 6, VII são 7, VIII são 8.
# X	Corresponde ao numeral 10.
#       IX são 9, XI é 11, etc..
# L	Corresponde ao numeral 50.
#       XL é o 40.
# C	Corresponde ao numeral 100.
# D	Corresponde ao numeral 500.
# M Corresponde ao numeral 1000.

# Exercício incompleto

def numRomana(numero):
    numerosRomanos = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    numeracaoNatural = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    result = ""

    for x in range(len(str(numero)) - 1, -1, -1):
        toLookFor = ""
        for j in range((len(str(numero)) - 1) - x, len(str(numero))):
            if toLookFor: toLookFor += "0"
            else: toLookFor += str(numero)[j]
        print("Looking for: " + toLookFor)
        for i in range(len(numeracaoNatural)):
            if int(toLookFor) == numeracaoNatural[i]:
                result += numerosRomanos[i]
                break
            else:
                if int(toLookFor) < numeracaoNatural[i]:
                    for j in range(int(str(toLookFor)[0])):

                    break
    return result

try:
    while True:
        try:
            num = int(input("Número: "))
            if num >= 1 and num <= 999: break
        except:
            continue
    print("Em numeração Romana: " + str(numRomana(num)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
