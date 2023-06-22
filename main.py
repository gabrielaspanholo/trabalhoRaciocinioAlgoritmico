#FONTE: https://br.investing.com/crypto/bitcoin/historical-data


import csv

def calcular_media(valores):
    return sum(valores) / len(valores)

maior_valor = None
valores = []

with open('database1.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    
    next(leitor_csv)
    
    for linha in leitor_csv:
        valor = float(linha[1])
        
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
        
        valores.append(valor)

media = calcular_media(valores)

print('Maior valor do BITCION no ultimo mes:', maior_valor)
print('Média entre os valores do BITCOIN no ultimo mes:', media)
