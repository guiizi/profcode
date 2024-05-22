def calculaArea(base, altura):
    area = base * altura / 2
    return area 

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

print("A area do tringulo é 2.%f cm²"%calculaArea(base,altura))
print("Um metodo pode ser utilizado quantas vezes necessarias")      
print(calculaArea(8,5))
print(calculaArea(10,10))
print(calculaArea(2,5))