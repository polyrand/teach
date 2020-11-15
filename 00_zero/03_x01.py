altura_actual = 0.5
altura_torre = 114
altura_caja = 0.5

while altura_actual < altura_torre:
    dias += 1
    cajas *= 2
    
    altura_actual = cajas * altura_caja