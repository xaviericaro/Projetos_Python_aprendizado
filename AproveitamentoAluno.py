print("-----------------------------------")
print("     Escola Capivara Cansada       ")
print("      Aproveitamento Aluno         ")
print("-----------------------------------")
print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())
media = (nota1 + nota2) / 2
if media >= 9 and media <= 10:
    print("Aproveitamento: A")
elif media >= 8 and media <9:
    print("Aproveitamento: B")
elif media >= 7 and media <8:
    print("Aproveitamento: C")
elif media >= 6  and media <7:
    print("Aproveitamento: D")
elif media >= 5 and media <6:
    print("Aproveitamento: E")
else:
    print("Aproveitamento: F")
print("A média do aluno é: ", media)
print("------------------------------------")