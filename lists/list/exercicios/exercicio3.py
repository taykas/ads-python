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

for i in range(len(meses)):
    if lista_temp[i] >= media:
        resumo_meses.append(lista_temp[i],meses[i])


print(f"Média de temperatura anual: {media}")

for i in range(len(resumo_meses)):
    print(f"Meses com maior temp: {resumo_meses[i]}")
