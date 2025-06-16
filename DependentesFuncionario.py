print("===========================================")
print("            Reajuste Salarial              ")
print("===========================================")
print("Esse programa calcula o aumento salarial de um funcionário com base na quantidade de dependentes.")
print("Qual o nome do Funcionário?")
nome = input()
print("Qual o salário do Funcionário? (R$xxxx)")
sal = float(input())
print("Qual a qualtidade de dependentes?")
dep = int(input())
if dep == 0:
    print("O novo salário do funcionnário", nome,"é: ", sal + ( sal * 5/100))
elif dep > 1 and dep <= 3:
    print("O novo salário do funcionario", nome,"é: ", sal + ( sal * 10/100))
elif dep >= 4 and dep <= 6:
    print("O novo salário do funcionario", nome,"é: ", sal + ( sal * 15/100))
else:
    print("O novo salário do funcionario", nome,"é: ", sal + ( sal * 20/100))
print("-------------------------------------------")