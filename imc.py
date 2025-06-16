print("Massa (kg):")
massa = float(input())
print("Altura (m): ")
altura = float(input())
imc = massa / (altura ** 2)
print("------------------------------------------------------")
print("IMC: ", imc)
if imc < 17:
    print("Muito abaixo do peso")
elif imc >= 17 and imc < 18.49:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidade I")
elif imc >= 35 and imc < 40:
    print("Obesidade II (severa)")
else:
    print("Obesidade III (mórbida)")
print("------------------------------------------------------")
print("IMC calculado com sucesso!")
print("------------------------------------------------------")