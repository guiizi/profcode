turno = input("DIGITE SEU TURNO: ")
horas = float(input("informe suas horas trabalhadas:"))
n = horas * 45.00
m = horas * 37.50
if turno == "n" or turno == "N":
    print("você recebe: R$", n)
else:
    print("você recebe: R$", m)