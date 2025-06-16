# Calculadora que realiza operação de soma, subtração, multiplicação e divisão, raiz quadrada e potênciação.
import math

def ler_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

while True:
    print("========= Escolha uma operação =========")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Potenciação")
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, digite um número válido")
        continue

    if opcao == 1:
         num1, num2 = ler_dois_numeros()
         print(f"{num1} + {num2} = {num1 + num2}")

    elif opcao == 2:
        num1, num2 = ler_dois_numeros()
        print(f"{num1} - {num2} = {num1 - num2}")

    elif opcao == 3:
         num1, num2 = ler_dois_numeros()
         print(f"{num1} * {num2} = {num1 * num2}")

# Indentifica se o usuario digitou 0 para não dividir por zero.
    elif opcao == 4:
        num1, num2 = ler_dois_numeros()
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("❌ Erro: Não é possível dividir por zero.")

# Só aceita um numero positivo para calcular a raiz quadrada.
    elif opcao == 5:
        num = float(input("Digite o número: "))
        if num >= 0:
            print(f"A raiz quadrada de {num} é {math.sqrt(num)}")
        else:
            print("❌ Não é possível calcular a raiz de número negativo.")

    elif opcao == 6:
        base = float(input("Digite o valor da base: "))
        expoente= float(input("Digite o valor do expoente: "))
        print(f"{base} elevado a {expoente} é igual a {math.pow(base, expoente)}")

    else:
        print("❌ Opção inválida!")
        print("Escolha uma opção válida entre 1 e 6.")

    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == 'n':
        print("👋 Valeu por usar a SmartCalc!")
        break
    elif continuar.lower() != 's':
        print("❌ Opção inválida. Encerrando...")
        break
# Fim do código