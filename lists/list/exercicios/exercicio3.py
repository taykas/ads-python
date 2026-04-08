meses = [
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

lista_temp = []
resumo_meses = []
media = 0

for mes in meses:
    temp = float(input(f"Temperatura média no mes de {mes}: "))
    lista_temp.append(temp)

media = sum(lista_temp) / len(lista_temp)

print(f"Média de temperatura anual: {media}")

print(f"Meses que tiveram temperatura maior que a média ({media:.1f})")

for i in range(len(meses)):
    if lista_temp[i] > media:
        print(f"mes: {meses[i]} - temp: {lista_temp[i]}")

