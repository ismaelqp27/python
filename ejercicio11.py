cantidad = float(input("Introduce la cantidad depositada: "))
interes = 0.04 
for año in range(1, 4):
    cantidad *= (1 + interes)
print(f"El capital tras 3 años es: {cantidad:.2f} euros")
