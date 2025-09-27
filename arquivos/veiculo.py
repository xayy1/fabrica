import csv

dados = 'veiculos.csv'#armezena o endreço do csv em uma variavel

with open(dados, "r") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=",")

    for linha in leitor:
        print(linha)