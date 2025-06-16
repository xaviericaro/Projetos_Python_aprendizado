apto = True
print("---------------------------------------")
print("       DEPARTAMENTO DE TRÂNSITO        ")
print("---------------------------------------")
print("Ano atual (yyyy): ")
ano = int(input())
print("Ano de Nascimento (yyyy): ")
nascimento = int(input())
print("------------------------------------------------------")
idade = ano - nascimento
print("Idade: ", idade)
if idade > 18:
    apto = True
    print("Apto para tirar CNH!")
else:
    apto = False
    print("Não está apto para tirar CNH!")
print("------------------------------------------------------")