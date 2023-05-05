while True:
    binario = input("Ingrese un número binario: ")
    if set(binario) - set("01"):
        print("La cadena ingresada no representa un número binario.")
    else:
        decimal = int(binario, 2)
        print("El número en representación decimal es:", decimal)
        break