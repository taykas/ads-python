n1 = float(input("nota bimestre 1: "))
n2 = float(input("nota bimestre 2: "))
n3 = float(input("nota bimestre 3: "))
n4 = float(input("nota bimestre 4: "))

faltas_aluno = int(input("Digite o número de faltas: "))

faltas = 100 - (faltas_aluno * 100) / 40
media = (n1+n2+n3+n4) / 4

if media < 7.0 and faltas < 75.0:
    print(f'aluno reprovado por média {media} e porcentagem de presença de {faltas}%') 
elif media >= 7.0 and faltas < 75.0:
    print(f'aluno reprovado por porcentagem de presença de {faltas}%')
else:
    print(f"aluno aprovado com média de {media} e porcentagem de presença de {faltas}%")
