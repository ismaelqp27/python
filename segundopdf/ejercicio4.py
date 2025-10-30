telefono = input("Teléfono (+34-xxxxxxxxx-yy): ")
partes = telefono.split("-")
print("Número sin prefijo ni extensión:", partes[1])
