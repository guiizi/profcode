compra = float(input("digite o valor da compra:"))
if compra > 200:
    desconto = compra - (compra * 0.2)
    print(f"vc tem o direito a 20% de desconto. o valor da compra foi de {desconto:.2f}")
else:
    print(f"vc nao tem direito a desconto. o valor da compra foi de {compra:.2f}")
    