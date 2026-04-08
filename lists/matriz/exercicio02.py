m = []

tam = int(input("Digite o tamanho da matriz desejada: "))

for i in range(tam):
    linha = []
    for j in range(tam):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    m.append(linha)

for i in range(tam):
    for j in range(tam):
        print(m[i][j], end=" ")
    print("\n")