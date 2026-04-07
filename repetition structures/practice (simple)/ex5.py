num = int(input("Digite o numerador: "))
exp = int(input("digite o expoente: "))
result = 1

for i in range(exp):
    result *= num

print(num, "elevado a", exp, "é igual a", result)