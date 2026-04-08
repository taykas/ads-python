# exemplo de matriz
m = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

print(m[0][2])

# coordenadas = []
# for i in range(3):
#     x = int(input("Insira um valor de x: "))
#     y = int(input("Insira um valor de y: "))
#     coordenadas.append([x, y])
# print(coordenadas)

for i in range(len(m)):
    for j in range(len(m)):
        print(m[i][j])

m.append([333])
m.append(444)
m[0].append(111)
m[1].append(111222)

print(m)