#exemplo 4 de FOR
for i in range(10):
    print(i, end=" ")
    
#for 5
for i in range(3, 8):
    print(i, end=" ")
    #print(i) pode ser
    
for i in range(0, 21, 2):
    print(i, end=" ")
    
for i in range(5, 20, 3):
    print(i, end=" ")

num = int(input("DIGITE O NUMERO DA TABAUDA:"))    
for i in range(11): 
    print("%d * %d = %d" (num, i, num*i))
    #print(i*num)
