cesta = {}
total = 0
continuar = True

while continuar:
    articulo = input("¿Qué artículo quieres añadir? ")
    precio = float(input("¿Cuánto cuesta " + articulo + "? "))
    
    cesta[articulo] = precio
     
    respuesta = input("¿Quieres añadir más cosas? (si/no): ")
    if respuesta.lower() == "no":
        continuar = False

print("\n--- LISTA DE LA COMPRA ---")
for articulo, precio in cesta.items():
    print(articulo, ":", precio)
    total = total + precio

print("\nEl coste total es:", total)