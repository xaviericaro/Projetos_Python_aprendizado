print("----- PIZZARIA CAPIVARA -----")
print("_____CARDÁPIO - PREÇOS_______")
print(" ")
print("*****PIZZAS - SABORES********")
print(" CALABRESA, FRANGO, CATUPIRY")
print("*****PIZZAS - TAMANHO********")
print("  PIZZA PEQUENA   R$ 25,00  ")
print("  PIZZA MÉDIA     R$ 38,00  ")
print("  PIZZA GRANDE    R$ 50,00  ")
print("*******REFRIGERANTES*********")
print("  COCA-COLA       R$ 6,40   ")
print("  GUARANÁ         R$ 6,00   ")
print("  FANTA           R$ 5,50   ")
print("_____________________________")
print(" ")

print("ESCOLHA O SABOR(1-3): ")
print("1 - CALABRESA")
print("2 - FRANGO")
print("3 - CATUPIRY")
pedidopizza = int(input())

print("DIGITE O TAMANHO DA PIZZA: ")
print("P - PEQUENA")
print("M - MÉDIA")
print("G - GRANDE")
tampizza = input().upper()

print("ESCOLHA O REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
pedidorefri = int(input())

# Define os nomes
if pedidopizza == 1:
    sabor = "CALABRESA"
elif pedidopizza == 2:
    sabor = "FRANGO"
elif pedidopizza == 3:
    sabor = "CATUPIRY"
else:
    sabor = "DESCONHECIDO"

# Preço da pizza
if tampizza == "P":
    tamanho = "PEQUENA"
    precopizza = 25.00
elif tampizza == "M":
    tamanho = "MÉDIA"
    precopizza = 38.00
elif tampizza == "G":
    tamanho = "GRANDE"
    precopizza = 50.00
else:
    tamanho = "DESCONHECIDO"
    precopizza = 0

# Preço do refri
if pedidorefri == 1:
    refri = "COCA-COLA"
    precorefri = 6.40
elif pedidorefri == 2:
    refri = "GUARANÁ"
    precorefri = 6.00
elif pedidorefri == 3:
    refri = "FANTA"
    precorefri = 5.50
else:
    refri = "DESCONHECIDO"
    precorefri = 0

# Soma total
precopagar = precopizza + precorefri
pedidos = f"{sabor}, {tamanho}, {refri}"

print("___________________________________________________________________")
print(f"O TOTAL A PAGAR É:  R$ {precopagar:.2f}")
print("___________________________________________________________________")
print(f"OS PEDIDOS FORAM {pedidos}")
print("___________________________________________________________________")
print("MUITO OBRIGADO PELA CONFIANÇA, SEU PEDIDO ESTÁ SENDO PREPARADO!!!")