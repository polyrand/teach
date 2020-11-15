if y < 2:
    x = "A"

elif y < 8:
    x = "B"

elif y == 10:
    x = "C"

else:
    y -= 1  # igual -> y = y - 1
    print("no se cumple nada")
    print("Y tiene el valor:", y)