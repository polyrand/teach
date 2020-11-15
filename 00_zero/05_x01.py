for nombre, valores in equipos.items():
        
    if sum(valores) > 200:
        print("el pc", nombres_pc[nombre], "tiene mas de 200")
    
    suma = 0