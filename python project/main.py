comando = input("Digite o comando desejado: ").upper()

while True:
    if(comando == "QUIT"):
        break

    match comando:
        case "ABOUT":
            print("===== Bem vindo(a) a Gestão de Álbuns da Thayna! <3 =====")

        case "ADD":
            num = int(input("Quantos álbuns deseja inserir? "))

            if num <= 0:
                print("Quantidade inválida, tente novamente!")
            else:
                print("Digite o nome dos álbuns:")
                for i in range(num):
                    nome_album = input(f"\n Álbum número {i}-> ")
                    print(f"Album: {nome_album}, adicionado com sucesso! :)")

        case "QUIT":
            print("Obrigada! saindo do programa...")

        case _:
            print("ERRO: Comando inválido, tente novamente!")

    comando = input("Digite o comando desejado: ").upper()

print("Até a próxima!")