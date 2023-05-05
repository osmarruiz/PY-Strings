def convertir(str):
    """ingresa una cedula y retorna la fecha de nacimiento"""
    anio=23
    r= int (str[8:10])
    return anio-r

cedula=input("Ingrese la cedula: ")
anios=convertir(cedula)
print(f"tiene {anios} años")