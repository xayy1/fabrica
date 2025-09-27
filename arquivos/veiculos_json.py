# importa as bibliotecas
import csv
import json

#cria as variaveis 
dados = 'veiculos.csv'#armezena o endreço do csv em uma variavel
dados_json = 'veiculos.json' 
veiculos = []

#abre o arquivo para leitura
with open(dados,'r',encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=",")
    for linha in leitor:
       veiculos.append(linha)

#abre o arquivo para escrita
with open(dados_json,'w',encoding='utf-8') as arquivo_json:
    json.dump(veiculos, arquivo_json,indent=2,ensure_ascii=False)

print(f"arquivo JSON gerado com sucesso: {dados_json}")