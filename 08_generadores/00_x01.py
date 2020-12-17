## Ejercicio: crear varios generadores:

# 1. Cada linea de mi archivo `data`
# 2. Cada elemento de un generador, convertido a numero entero
# 3. Cada elemento al cuadrado `**2` de un generador

#   * ¿Cuánto suman todos esos números que hemos elevado al cuadrado?

# 4. Crear una función generadora que me devuelva todos los múltiplos (infinitos) de un número.

from base64 import b64decode, b64encode
import requests

u1 = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3BvbHlyYW5kL2FkdmVudG9mY29kZV8yMDIwL21haW4vZDAxL2lucHV0X3AxLnR4dA=="


with open("input.txt", "w") as f:
    f.write(requests.get(b64decode(u1).decode()).text)


with open("input.txt") as f:
    data = f.read()

lineas = (elemento for elemento in data.split("\n"))

numeros = (int(e) for e in lineas)

cuadrados = (num**2 for num in numeros)


print(sum(cuadrados))


def multiplos(x):

    i = 1
    while True:
        yield x * i
        i += 1