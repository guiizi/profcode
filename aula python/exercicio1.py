#eleitor
idade = int(input("COLOQUE SUA IDADE:"))
if idade < 16:
     print("VOCE É NÃO-ELEITOR") 
elif idade >= 65 and idade <=18:
    print("VOCE É ELEITOR OBRIGATORIO")
else:
    print("VOCE É ELEITOR FACULTATIVO")
    
    #print("sua classe eleitoral é: %s" % categoria)
    #print(f"sua classe eleitoral é: {cayegoria}")
    #print("sua classe eleitoral é: , categoria")