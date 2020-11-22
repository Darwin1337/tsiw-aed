import os
import traceback

# [Ficha 06 - Ex. 05] - Lê a faturação mensal de uma empresa ao longo dos 12 meses do ano (de janeiro a dezembro)
# e determina o mês de maior faturação, o mês de menor faturação e a média mensal de faturação

def maiorFaturacao(faturacoes):
    # Se o valor maior pertencer a vários meses - mostrar todos
    if faturacoes.count(max(faturacoes)) > 1:
        result = "Meses com maior faturação:\n"
        for x in range(len(faturacoes)):
            if faturacoes[x] == max(faturacoes):
                result += meses[x] + " com uma faturação de: %.2f€" % max(faturacoes) + "\n"
        return result
    else: return "Mês com maior faturação:\n" + meses[faturacoes.index(max(faturacoes))] + " com uma faturação de: %.2f€" % max(faturacoes)

def menorFaturacao(faturacoes):
    # Se o valor menor pertencer a vários meses - mostrar todos
    if faturacoes.count(min(faturacoes)) > 1:
        result = "Meses com menor faturação:\n"
        for x in range(len(faturacoes)):
            if faturacoes[x] == min(faturacoes):
                result += meses[x] + " com uma faturação de: %.2f€" % min(faturacoes) + "\n"
        return result
    else: return "Mês com menor faturação:\n" + meses[faturacoes.index(min(faturacoes))] + " com uma faturação de: %.2f€" % min(faturacoes)

def mediaFaturacao(faturacoes):
    soma = 0.0
    for num in faturacoes:
        soma += num
    return "%.2f€" % float(soma / len(meses))

try:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    ftrMeses = []
    for mes in meses:
        while True:
            try:
                faturacao = float(str(input("Faturação do mês de " + mes + ": ")).replace(",", "."))
                if faturacao > 0.0:
                    ftrMeses.append(faturacao)
                    break
            except: continue
    print(maiorFaturacao(ftrMeses))
    print(menorFaturacao(ftrMeses))
    print("Média de faturação: " + mediaFaturacao(ftrMeses))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
