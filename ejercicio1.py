def convertir(str):
    """ingresa una cedula y retorna la fecha de nacimiento"""
    anio=2023
    r= int (str[8:10])
    if r <= 23:
        r +=2000
    else:
        r+=1900
    return anio-r

cedula=input("Ingrese la cedula: ")
anios=convertir(cedula)
print(f"tiene {anios} años")