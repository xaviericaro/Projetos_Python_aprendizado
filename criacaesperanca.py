print("----------------------------------------")
print("          CRIANÇA ESPERANÇA             ")
print("----------------------------------------")
print("Muito obrigado por ajudar a mudar a vida de milhares de crianças")
print(" [1] - para doar R$ 10,00")
print(" [2] - para doar R$ 25,00")
print(" [3] - para doar R$ 50,00")
print(" [4] - para doar outros valores")
print(" [5] - para cancelar")
print("----------------------------------------")
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    print("Sua doação de R$10,00 foi realizada com sucesso!")
elif opcao == 2:
    print("Sua doação de R$25,00 foi realizada com sucesso!")
elif opcao == 3:
    print("Sua doação de R$50,00 foi ealizada com sucesso!")
elif opcao == 4:
    print("Digite o valor que deseja doar: ")
    valor = float(input())
    print("Sua doação de R$" + str(valor) + " foi realizada com sucesso!")
elif opcao == 5:
    print("Obrigado por visitar nosso site!")
else:
    print("Opção inválida!")
print("----------------------------------------")
