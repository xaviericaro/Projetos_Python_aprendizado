while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Falou campeão! Até a proxima! 😎")
        break
    print("------------------------------------------------------")