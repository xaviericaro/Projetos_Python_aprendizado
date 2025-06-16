# Escolha o sabor da pizza, tamanho e bebida
print("========= Pizzaria Capivara Feliz =========")
print("Escolha o Sabor da Pizza")
print("1 - Calabresa")
print("2 - Portuguesa")
print("3 - Frango com Catupiry")
print("4 - Quatro Queijos")
print("5 - Marguerita")
print(" ")

sabor = int(input("Digite o número do sabor desejado: "))
if sabor <= 0 or sabor > 5:
    print("❌ Sabor inválido! Escolha um sabor entre 1 e 5.")
elif sabor == 1:
    print("Você escolheu a pizza de Calabresa.")
elif sabor == 2:
    print("Você escolheu a pizza Portuguesa.")
elif sabor == 3:
    print("Você escolheu a pizza de Frango com Catupiry.")
elif sabor == 4:
    print("Você escolheu a pizza Quatro Queijos.")
elif sabor == 5:
    print("Você escolheu a pizza Marguerita.")

print(" ")
print("========= Escolha o tamanho da Pizza =========")
print("1 - Pequena")
print("2 - Média")
print("3 - Grande")
print("4 - Gigante")
print(" ")

tam = int(input("Digite o número do tamanho desejado: "))
# Verifica se o tamanho da pizza é válido
# e se o usuário digitou um número entre 1 e 4.
if tam <= 0 or tam > 4:
    print("❌ Tamanho inválido! Escolha um tamanho entre 1 e 4.")
elif tam == 1:
    print("Você escolheu a pizza Pequena.")
elif tam == 2:
    print("Você escolheu a pizza Média.")
elif tam == 3:
    print("Você escolheu a pizza Grande.")
elif tam == 4:
    print("Você escolheu a pizza Gigante.")

print(" ")
print("========= Escolha a Bebida =========")
print("1 - Refrigerante")
print("2 - Suco")
print("3 - Água")
print(" ")
# Verifica se a bebida é válida
# e se o usuário digitou um número entre 1 e 3.
bebida = int(input("Digite o número da bebida desejada: "))

if bebida <= 0 or bebida > 3:
    print("❌ Bebida inválida! Escolha uma bebida entre 1 e 3.")
elif bebida == 1:
    print("Escolha o Refrigerante:")
    print("1 - Coca-Cola")
    print("2 - Guaraná")
    print("3 - Fanta")
    print("4 - Sprite")
    print(" ")
# Verifica se o refrigerante é válido
# e se o usuário digitou um número entre 1 e 4.
    refri = input("Digite o número do refigerante desejado: ")
    if refri == "1":
        print("Você escolheu Coca-Cola.")
    elif refri == "2":
        print("Você escolheu Guaraná.")
    elif refri == "3":
        print("Você escolhue Fanta.")
    elif refri == "4":
        print("Você escolheu Sprite.")
    else:
        print("❌ Refrigerante inválido! Escolha um refrigerante entre 1 e 4.")
    
elif bebida == 2:
    print(" ")
    print("Escolha o Suco:")
    print("1 - Laranja")
    print("2 - Limão")
    print("3 - Abacaxi")
    print("4 - Uva")
    suco = int(input("Digite o número do suco desejado: "))
# Verifica se o suco é válido
# e se o usuário digitou um número entre 1 e 4.
    if suco == 1:
        print("Você escolheu Suco de Laranja.")
    elif suco == 2:
        print("Você escolheu Suco de Limão.")
    elif suco == 3:
        print("Você escolheu Suco de Abacaxi.")
    elif suco == 4:
        print("Você escolheu Suco de Uva.")
    else:
        print("❌ Suco inválido! Escolha um suco entre 1 e 4.")

elif bebida == 3:
    print("Você escolheu Água.")
else:
    print("❌ Bebida inválida! Escolha uma bebida entre 1 e 3.")
print(" ")
print("========= Resumo do Pedido =========")
print(f"Sabor da Pizza: {sabor}")
print(f"Tamnho da Pizza: {tam}")
print(f"Bebida: {bebida}")
print("")
print("========= Obrigado pela preferência! =========")
print("Aguarde o entregador chegar na sua casa.")
# Fim do código