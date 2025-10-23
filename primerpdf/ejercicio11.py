cantidad = float(input("Introduce la cantidad depositada: "))
interes = 0.04 
for año in range(1, 4):
    cantidad *= (1 + interes)
print("el capital después de 3 años es:", + str(cantidad, 2))
