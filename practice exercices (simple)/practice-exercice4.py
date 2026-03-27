nome = input("Digite o nome da disciplina: ")
print("Digite em seguida suas notas: ")
n1 = float(input("-> "))
n2 = float(input("-> "))
n3 = float(input("-> "))
n4 = float(input("-> "))

media = (n1+n2+n3+n4) / 4
print("Sua média da Matéria:", nome, "é: ", media)