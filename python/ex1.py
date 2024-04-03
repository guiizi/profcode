valor_prestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem da multa pelo atraso (em %): "))
qtdedias = int(input("Digite a quantidade de dias de atraso: ")) 
prestacao = valor_prestacao + valor_prestacao * multa/100 * qtdedias
print (f"O valor da prestação atualizado é: R${prestacao:.2f}")  