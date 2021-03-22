# Opcion 1
for nombre, valores in equipos.items():

    if sum(valores) > 200:
        print("el pc", nombres_pc[nombre], "tiene mas de 200")


# Opcion 2
for nombre, valores in equipos.items():
    print(f"Iterando sobre {nombre}")
    print(f"Iterando con {valores}")

    suma = 0
    for v in valores:
        suma += v

    if suma > 200:
        print("el pc", nombres_pc[nombre], "tiene mas de 200")
