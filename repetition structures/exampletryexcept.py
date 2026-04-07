while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado:", num)

while True:
    try:
        num = float(input("Digite um número decimal: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado:", num)

while True:
    try:
        num = int(input("Digite um número inteiro entre 1 e 5: "))
        if 1 <= num <= 5:
            break
        else:
            print("O número deve estar entre 1 e 5.")
    except ValueError:
        print("Valor inválido")
print("Número validado:", num)