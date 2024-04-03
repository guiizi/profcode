luz=float(input("valor da conta de luz:"))
telefone=float(input("valor da conta telefonica:"))
agua=float(input("valor da conta de agua:"))
salario=float(input("salario:"))
totalcontas=luz+telefone+agua
if totalcontas > salario:
    print("salario insuficiente")
else:
    resto=salario - totalcontas
    print(f"vc pagou as contas, sobrou {resto:.2f}")