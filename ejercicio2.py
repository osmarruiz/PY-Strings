frase = input("Ingrese una frase: ")
vocales = 0
consonantes = 0
palabras = len(frase.split())

for letra in frase:
    if letra.isalpha():
        if letra.lower() in "aeiou":
            vocales += 1
        else:
            consonantes += 1

print("La frase ingresada tiene", vocales, "vocales y", consonantes, "consonantes")
print("La frase ingresada tiene", palabras, "palabras")