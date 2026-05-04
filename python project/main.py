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
        print("=-=-= ERRO: O arquivo está vazio ou corrompido. Os dados serão reiniciados. =-=-=")
        return []

# Quando QUIT, recebe a lista de albuns e salva o arquivo
def salvar_albuns(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

albuns = carregar_albuns()

# Gera id simples
def gerar_id(lista):
    if not lista:
        return 1
    return lista[-1]["id"] + 1

while True:
    comando = input("\n\nDigite o comando desejado *ABOUT | ADD | LIST | UPDATE | DELETE | QUIT* -> ").strip().upper()

    if  not comando:
        print("\n=-=-= ERRO: Comando vazio! Tente novamente. =-=-=")
        continue

    if comando.isnumeric():
        print("\n=-=-= ERRO: Comando não pode ser número! =-=-=")
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
                        print("\n=-=-= ERRO: Valor vazio! Digite um número. =-=-=")
                        continue

                    if not valor.isdigit():
                        print("\n=-=-= ERRO: Erro de digitação! Digite apenas números. =-=-=")
                        continue

                    num = int(valor)

                    if num <= 0:
                        print("\n=-=-= ERRO: Quantidade inválida! O número deve ser maior que zero. =-=-=")
                        continue

                    break

                except ValueError:
                    print("\n=-=-= ERRO: Erro de conversão! Tente novamente. =-=-=")

            print(f"\nQuantidade Desejada: {num}, perfeito! \n\n=-=-= Cadastro de Álbuns =-=-=")

            for i in range(num):
                while True:
                    nome_album = input(f"\nÁlbum número {i+1}: ").strip()

                    if not nome_album:
                        print("\n =-=-= ERRO: Nome não pode ser vazio! =-=-=\n")
                        continue

                    break
                
                albuns.append({
                    "id": gerar_id(albuns),
                    "nome": nome_album,
                    "status": "pendente"
                })

                print(f"\nAdicionado com sucesso! :)")

        case "LIST":
            if not albuns:
                print("\nNenhum álbum cadastrado.\n")
            else:
                for album in albuns:
                    print(f"\n=-=-= ID: {album['id']} | Nome: {album['nome']} | Status: {album['status']}")

        case "UPDATE":
            try:
                id_busca = int(input("\nDigite o ID do álbum: "))
            except ValueError:
                print("=-=-= ERRO: ID inválido! =-=-=")
                continue

            for album in albuns:
                if album["id"] == id_busca:
                    print("\n=-= Escolha o novo status =-=")
                    print("1 - Concluído")
                    print("2 - Em andamento")

                    try:
                        opcao = int(input("Opção: ").strip())

                        if opcao == 1:
                            novo_status = "concluído"
                        elif opcao == 2:
                            novo_status = "em andamento"
                        else:
                            print("ERRO: Opção inválida!")
                            break

                    except ValueError:
                        print("ERRO: Digite apenas números (1 ou 2)!")
                        break

                    album["status"] = novo_status
                    print("Álbum atualizado!")
                    break

            else:
                print("=-=-= ERRO: Álbum não encontrado! =-=-=")

        case "DELETE":
            try:
                id_busca = int(input("Digite o ID do álbum: "))
            except ValueError:
                print("=-=-= ERRO: ID inválido! =-=-=")
                continue

            for album in albuns:
                if album["id"] == id_busca:
                    albuns.remove(album)
                    print("Álbum removido!")
                    break
            else:
                print("=-=-= ERRO: Álbum não encontrado! =-=-=")

        case "QUIT":
            salvar_albuns(albuns)
            print("\nSUCESSO: Dados salvos com sucesso!")
            print("Obrigada! saindo do programa...")
            break

        case _:
            print("\n=-=-= ERRO: Comando inválido! Use: ABOUT | ADD | LIST | UPDATE | DELETE | QUIT =-=-=")

    while True:
        comando = input("\nDigite o comando desejado *ABOUT | ADD | LIST | UPDATE | DELETE | QUIT* -> ").strip().upper()

        if not comando:
            print("\n=-=-= ERRO: Comando vazio! Tente novamente. =-=-=")
            continue

        if comando.isnumeric():
            print("\n=-=-= ERRO: Comando não pode ser número! =-=-=")
            continue

        break

print("\n =-=-= Até a próxima! =-=-=")