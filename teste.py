# Tentar executar o código que pode apresentar um erro
try:
    #Solicitar ao usuário que digite dois número e reliza a divisão 
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 / num2 

# Caso o erro seja algum valor não numérico (digite textos)
except ValueError as ve:
    print(f"Seu cálculo apresentou o erro {ve}")
    print("Digite algarismos numéricos")
# Caso o erro seja de divisão por 0 
except ZeroDivisionError:
    print("Divisão por zero não é permitida")
# Caso o erro seja outro não tratado anteriormente
except:
    print("Digite números válidos")

else:
    print(f"O resulto da divisão é {resultado}")

finally:
    print("Operação finalizada")