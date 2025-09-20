try: # tentar

    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

except: # Exceção
    print("Divisões por zero nao sao possiveis")



