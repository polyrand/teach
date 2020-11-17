def suma(a, b):

    if type(a) == str:
    # la forma correcta sería usar la función isinstance()
    # if isinstance(a, str):
        print(f"el parametro a, con datos: {a} es texto y debería ser un número")
        return
    
    if type(b) == str:
        print(f"el parametro b, con datos: {b} es texto y debería ser un número")
        return
    
    resultado = a + b
    print("El resultado es:", resultado)
    
    return resultado