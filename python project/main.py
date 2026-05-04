import json

ARQUIVO = "portfolio.json"

# Lê e valida o arquivo
def carregar_albuns():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("\n =-=-= ERRO: Arquivo não encontrado. Um novo será criado automaticamente. =-=-=\n")
        return []
    except json.JSONDecodeError:
        print("ERRO: O arquivo está vazio ou corrompido. Os dados serão reiniciados.")
        return []

# Quando QUIT, salva o arquivo
def salvar_albuns(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

albuns = carregar_albuns()

while True:
    comando = input("\nDigite o comando desejado *ABOUT | ADD | QUIT* -> ").strip().upper()

    if  not comando:
        print("\nERRO: Comando vazio! Tente novamente.")
        continue

    if comando.isnumeric():
        print("\nERRO: Comando não pode ser número!")
        continue
    break

while True:
    match comando:
        case "ABOUT":
            print("\n =-=-=-=-= Bem vindo(a) a Gestão de Álbuns da Thayna! <3 =-=-=-=-=\n" \
            "\nAqui você encontra os álbuns na lista de espera para escutar da Thayna!\n" \
            "Esse projeto está sendo desenvolvido em Python na matéria de *RACIOCÍNIO COMPUTACIONAL*\n" \
            "Fique a vontade para utilizar dessa ferramenta para não perder nenhum álbum!")

        case "ADD":
            while True:
                try:
                    valor = input("\nQuantos álbuns deseja inserir? ").strip()

                    if not valor:
                        print("\nERRO: Valor vazio! Digite um número.")
                        continue

                    if not valor.isdigit():
                        print("\nERRO: Erro de digitação! Digite apenas números.")
                        continue

                    num = int(valor)

                    if num <= 0:
                        print("\nERRO: Quantidade inválida! O número deve ser maior que zero.")
                        continue

                    break

                except ValueError:
                    print("\nERRO: Erro de conversão! Tente novamente.")

            print(f"\nQuantidade Desejada: {num}, perfeito! \n\n=-=-= Cadastro de Álbuns =-=-=")

            for i in range(num):
                while True:
                    nome_album = input(f"\nÁlbum número {i+1}: ").strip()

                    if not nome_album:
                        print("\n =-=-= ERRO: Nome não pode ser vazio! =-=-=\n")
                        continue

                    break

                albuns.append(nome_album)
                print(f"\nÁlbum: {nome_album}, adicionado com sucesso! :)")

        case "QUIT":
            salvar_albuns(albuns)
            print("\nSUCESSO: Dados salvos com sucesso!")
            print("Obrigada! saindo do programa...")
            break

        case _:
            print("\nERRO: Comando inválido! Use: ABOUT | ADD | QUIT")

    while True:
        comando = input("\nDigite o comando desejado: ").strip().upper()

        if not comando:
            print("\nERRO: Comando vazio! Tente novamente.")
            continue

        if comando.isnumeric():
            print("\nERRO: Comando não pode ser número!")
            continue

        break

print("\n =-=-= Até a próxima! =-=-=")