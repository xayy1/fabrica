try:
    print("Converte Celsius para Fahrenheit")

    elsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}°F')

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico ")

except Exception as e:
    print(f"Ocorreu erro inesperado: {e}. Por favor, tente novamento.")