a = int(input("Enter value: \nside A: "))
b = int(input("side B: "))
c = int(input("side C: "))


if (a+b > c) or (b+c > a) or (a+c > b):
    if a != b and b != c and c != a:
        print("\n-> Escaleno")
    elif (a != b and b == c and c != a ) or (a == b and b != c and c != a ) or (a != b and b != c and c == a ):
        print("\n-> Isósceles")
    else:
        print("\n-> Equilátero")
else:
    print("Não é um triângulo!")