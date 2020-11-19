import mis_funciones

usuarios = mis_funciones.leer_json("users.json")

print("Hola, introduce un nuevo valor")

valor = input("Valor: ")

usuarios["andrea"] = valor

mis_funciones.guardar_json(usuarios, "users_updated.json")

print("JSON actualizado")
