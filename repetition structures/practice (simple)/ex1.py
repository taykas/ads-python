numimpar = 0
numpar = 0
cont = 0

while(cont != 10):
    try:
        num = int(input("Digite um númer: "))
        if(num % 2 == 0):
            numpar+=1
        else:
            numimpar+=1

        cont += 1
    except:
        print("Valor inválido, tente novamente")
    
print(f"dos 10 num, {numpar} são pares, {numimpar} são ímpares")