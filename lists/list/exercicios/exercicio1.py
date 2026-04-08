lista = []
meida = 0
maior_media = []
menor_media = []

print("Digite os números: ")

for i in range(6):
    lista.append(int(input(f"{i} -> ")))

media = sum(lista) / len(lista)

for i in range(len(lista)):
    if lista[i] >= media:
        maior_media.append(lista[i])
    else:
        menor_media.append(lista[i])

print(media)
print(maior_media)
print(menor_media)