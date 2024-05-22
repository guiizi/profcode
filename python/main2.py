import trigonometria 
catO = float(input("Cateto oposto:"))
catA = float(input("Cateto adjascente:"))

print("O seno é : %.2f"%trigonometria.seno(catO, catA))
print("O cosseno é : %.2f"%trigonometria.cosseno(catO, catA))
print("O tangente é : %.2f"%trigonometria.tangente(catO, catA))