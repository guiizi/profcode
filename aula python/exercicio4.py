#media alunos WHILE
contador = 1 
while contador <=10:
    nota1 = float(input("DIGITE A PRIMEIRA NOTA:"))
    nota2 = float(input("DIGITE A SEGUNDA NOTA:"))
    media = (nota1 + nota2)/2
    print("A MÉDIA É %.2f" % media)
    contador = contador + 1
    