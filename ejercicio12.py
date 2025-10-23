precio_barra = 3.49
descuento = 0.6

barras = int(input("Número de barras no del día: "))

precio_total = barras * precio_barra * (1 - descuento)

print("Precio barra:", precio_barra)
print("Descuento:", descuento)
print("Total:", precio_total)
