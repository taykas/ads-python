comando = input("Digite o comando desejado: ")

while(comando.upper() != "QUIT"):
    match comando.upper():
        case "ABOUT":
            print("===== Bem vindo(a) a Gestão de Albuns da Thayna! <3 =====")
        case "QUIT":
            print("Obrigada! saindo do programa...")
        case _:
            print("ERRO: Comando inválido, tente novamente!")

    comando = input("Digite o comando desejado: ")
print("Até a próxima!")