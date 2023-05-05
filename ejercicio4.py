cadena = input("Ingrese una cadena: ")
mayusculas = 0

for letra in cadena:
    if letra.isupper():
        mayusculas += 1

print("La cadena ingresada tiene", mayusculas, "letras mayúsculas")