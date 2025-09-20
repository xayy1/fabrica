import requests

cep = input("Digite seu cep: ")
via_cep = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(via_cep)

print(requisicao)

print(f"CEP: {requisicao.json()['cep']}")
print(f"LOGRADOURO: {requisicao.json()['logradouro']}")
print(f"BAIRRO: {requisicao.json()['bairro']}")
print(f"LOCALIDADE: {requisicao.json()['localidade']}")
print(f"ESTADO: {requisicao.json()['estado']}")