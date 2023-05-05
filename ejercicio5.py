cadena = input("Ingrese una cadena: ")

if any(char.isdigit() for char in cadena):
    print("La cadena ingresada contiene dígito")
else:
    print("La cadena ingresada no contiene dígito")