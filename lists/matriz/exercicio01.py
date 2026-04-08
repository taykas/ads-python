m = []
m2 = []

result = []

soma = 0


print('matriz 1')
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"digite o num na linha {i} coluna {j}: "))
        linha.append(num)
    m.append(linha)


print("matriz 2")
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"digite o num na linha {i} coluna {j}: "))
        linha.append(num)
    m2.append(linha)

print(m)
print(m2)

for i in range(3):
    for j in range(3):
        print(f"{m[i][j]}", end="  ")
    print("\n")

for i in range(3):
    lista = []
    for i in range(3):
        soma = (m[i][j] + m2[i][j])
        lista.append(soma)
    soma = 0
    result.append(lista)

print(result)
