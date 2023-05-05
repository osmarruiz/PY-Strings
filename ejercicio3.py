cadena = input("Ingrese una cadena: ")
espacios = 0

for letra in cadena:
    if letra == " ":
        espacios += 1

print("La cadena ingresada tiene", espacios, "espacios en blanco")