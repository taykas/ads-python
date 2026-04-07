user_senha = "teste"
user_login = "so eu"

while True:
    senha = input("Digite a senha: ")
    login = input("Digite o Login: ")

    if(senha != user_senha or login != user_login):
        print("erro! login ou senha incorretos, tente novamente...")
    else:
        print("Sucesso!")
        break