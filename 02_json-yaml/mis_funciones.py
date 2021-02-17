import json


def leer_json(nombre):
    
    with open(nombre) as f:
        contenidos_archivo = f.read()
    obj = json.loads(contenidos_archivo)

    return obj


def guardar_json(obj, nombre):
    
    cadena_json = json.dumps(obj)
    
    with open(nombre, "w") as f:
        
        f.write(cadena_json)
        
    return cadena_json
