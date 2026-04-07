comando = input("Digite o comando desejado: ").upper()

while(comando!= "QUIT"):
    match comando:
        case "ABOUT":
            print("===== Bem vindo(a) a Gestão de Albuns da Thayna! <3 =====")
        case "QUIT":
            print("Obrigada! saindo do programa...")
        case _:
            print("ERRO: Comando inválido, tente novamente!")

    comando = input("Digite o comando desejado: ").upper()
print("Até a próxima!")