soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

print("Calculadora Lambda")
print("[1]soma\n[2] Subtração\n[3]Multiplicação\n[4]Divisão\n[0] Sair")
while True:
    op = int(input("Digite uma opção:"))
    if op ==0:
        print("Obrigado por utilixar nossa calculadora.")
        break
    elif str(op) not in '1234':
        print("Opção inválida")
    else:
        a = float(input("Digite o primeiro numero:")) 
        b = float(input("Digite o segundo numero:")) 
        if op==1: print(soma(a,b))
        elif op==2: print(subtracao(a,b))
        elif op==3: print(multiplicacao(a,b))
        else: print(divisao(a,b))
        
        
