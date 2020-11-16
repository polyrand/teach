# Opcion 1
altura_actual = 0.5
altura_torre = 114
altura_caja = 0.5

while altura_actual < altura_torre:
    dias += 1
    cajas *= 2
    
    altura_actual = cajas * altura_caja
    
    
# Opcion 2
num_dias = 1
num_cajas = 1

# variables medidas en metros
altura_torre = 114
tamaño_caja = 0.5
altura_cajas = tamaño_caja * num_cajas

print("Empezamos con una altura de cajas:", altura_cajas)

### Variables

while altura_cajas < altura_torre:
    num_dias += 1
    print("Dia", num_dias)

    num_cajas *= 2
    print("Cajas", num_cajas)

    altura_cajas = tamaño_caja * num_cajas
    print("Altura", altura_cajas)

## CODE