#numero binario
num = input("digite um numero binário:")
n = len(num)-1
decimal = 0
for d in num:
    decimal = decimal + int(d)*2**n
    n = n-1 
    
print("o binário de %s equivale a %d na base decimal." %(num, decimal))
    