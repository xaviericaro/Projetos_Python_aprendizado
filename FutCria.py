print("------------------------------------")
print("       BANGU X MADUREIRA FC         ")
print("------------------------------------")
print("Quantos gols o Bangu fez? ")
gols1 = int(input())
print("Quantos gols o Madureira fez? ")
gols2 = int(input())
if gols1 > gols2:
    dif = gols1 - gols2
else: 
    dif = gols2 - gols1
print("-------------------------------------")
if dif == 0:
    print("Status do jogo: Empate")
elif dif >= 1 and dif <= 3:
    print("Status do jogo: Jogo normal")
elif dif >= 4 and dif <= 7:
    print("Satus do jogo: Goleada")
else:
    print("Status do jogo: Jogo anormal")
    print("Você digitou os dados corretos?")
print("--------------------------------------")