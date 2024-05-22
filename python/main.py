import metodo

a = int(input("Digite a:"))
b = int(input("Digite b:"))

op = int(input("1-soma\n2-Subtração:\nDigite uma opção:"))
if op ==1:
    print(metodo.somaValores(a,b))
elif op ==2:
    print(metodo.subtraiValores(a, b))
else:
    print("Opçãp inválida") 
    
metodo.fim()

