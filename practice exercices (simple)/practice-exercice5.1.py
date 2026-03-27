valor = float(input("Informe qual o preço: "))
qtd = int(input("Informe qual a quantidade comprada: "))

total = valor*qtd
total_desconto = total-(total*0.15)

print("O total da compra foi de R$", total)
print("O total da compra com 15% de desconto foi de R$", total_desconto)