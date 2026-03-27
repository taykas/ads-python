# entrada de dados
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")


# obtém a data atual
data_atual = input("Digite o dia de hoje (dd/mm/aaaa): ")

# separa a data de nascimento em dia, mês e ano
dia_nascimento = int(data_nascimento[:2])
mes_nascimento = int(data_nascimento[3:5])
ano_nascimento = int(data_nascimento[6:])

# separa a data atual em dia, mês e ano
dia_atual = int(data_atual[:2])
mes_atual = int(data_atual[3:5])
ano_atual = int(data_atual[6:])

# calcula a idade em anos
idade = ano_atual - ano_nascimento

# verifica se já fez aniversário este ano
if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

# exibe a idade
print("Sua idade é:", idade, "anos")