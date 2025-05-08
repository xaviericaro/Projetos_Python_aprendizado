print("============== Conversor de Temperatura ==============")
print("Escolha uma oção de conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - fahrenheit para Celsius")
print("3 - Celsius para Kelvin")
print("4 - Kelvin para Celsius")
print("5 - Fahrenheit para Kelvin")
print("6 - Kelvin para Fahrenheit")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    celsius = float(input("Temperatura em Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")

elif opcao == 2:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    celsius = (fahrenheit -32) / 1.8
    print(f"{fahrenheit}°F é igual a {celsius}°C")

elif opcao == 3:
    celsius = float(input("Temperatura em Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}°C é igual a {kelvin}°K")

elif opcao == 4:
    kelvin = float(input("Temperatura em Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}°K é igual a {celsius}°C")

elif opcao == 5:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    print(f"{fahrenheit}°F é igual a {kelvin}°K")

elif opcao == 6:
    kelvin = float(input("Temperatura em Kelvin: "))
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    print(f"{kelvin}°K é igual a {fahrenheit}°F")

else:
    print("Opção inválida!")
    print("Escolha uma opção válida entre 1 e 6.")
