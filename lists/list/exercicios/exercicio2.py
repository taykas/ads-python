lista1 = []
lista2 = []
lista3 = []

print("Digite ")

for i in range(5):
    num = int(input("lista 1 -> "))
    lista1.append(num)
    lista3.append(lista1[i])

    num2 = int(input("lista 2 ->" ))
    lista2.append(num2)
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)