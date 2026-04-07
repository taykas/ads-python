media = 0
contador = 0

while True:
    num = float(input("Digite um número: "))

    if num == 0:
        print(f"Media: {media / contador}")

    media+=num
    contador +=1
