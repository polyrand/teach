
import json


def leer_json(nombre):
    with open(nombre) as f:
        contenidos_archivo = f.read()
        obj = json.loads(contenidos_archivo)

    return obj


def guardar_json(obj, nombre):
    with open(nombre, "w") as f:
        cadena_json = json.dumps(obj)
        f.write(cadena_json)
