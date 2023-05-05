import re

cadena = input("Ingrese una cadena: ")
numeros = re.findall(r'\d+', cadena)

if len(numeros) == 0:
    print("La cadena ingresada no tiene números")
else:
    print("La cadena ingresada tiene", len(numeros), "números:")
    for numero in numeros:
        print("- el", numero)