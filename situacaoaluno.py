print("---------------------------------------")
print("        ESCOLA CAPIVARA CANSADA        ")
print("---------------------------------------")
print("Digite a primeira nota do aluno: ")
nota1 = float(input())
print("Digite a segunda nota do aluno: ")
nota2 = float(input())
media = (nota1 + nota2) / 2
print("----------------------------------------")
print("Média: ", media)
if media >= 6:
    print("Aluno Aprovado")
elif media >= 4 and media < 5.5:
    print("Aluno de recuperação")
elif media < 4:
    print("Aluno reprovado")
print("----------------------------------------")