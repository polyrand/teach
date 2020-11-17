lista_miembros.append("ricardo")

# A ver si el último valor de la lista es "ricardo":

lista_miembros[-1]

x = 0

for nombre in lista_miembros:
    if nombre == "ricardo":
        print("ricardo está aquí")
    else:
        print("student")

    if "i" in nombre:
        x += 1
