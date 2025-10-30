nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Unidades: "))
total = precio * unidades

print(f"{nombre} {precio:08.2f} {unidades:03d} {total:010.2f}")
