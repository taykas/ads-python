word = input("Digite um texto: ")

for letra in word:
    if letra not in "aeiou":
        print(letra) 