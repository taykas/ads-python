print("=-=-= Esse código tem como função mapear as notas na faculdade de ADS - PUC =-=-=")

import json

ARQUIVO = "materias.json"

materias = {}

# ==================== FUNÇÕES =======================

def carregar_cadastro():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("\n =-=-= ERRO: Arquivo não encontrado. Um novo será criado automaticamente. =-=-=\n")
        return []
    except json.JSONDecodeError:
        print("=-=-= ERRO: O arquivo está vazio ou corrompido. Os dados serão reiniciados. =-=-=")
        return []

def interacao():
    while True: 
        try:
            num = int(input("Quantidade matérias: "))
            break
        except ValueError:
            print("Erro: input inválido!")
    return num

# ===================================================

for i in range(interacao()):
    nome = input("Nome da Matéria: ")
    materias[i+1] = nome

print(materias)