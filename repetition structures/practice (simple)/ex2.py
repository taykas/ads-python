maior = 1
menor = -1

for i in range (5):
    num = int(input("Digite um número: "))

    if(num > maior):
        maior = num
    else:
        menor = num
print(f"Maior: {maior}, menor: {menor}")