productos = input("Productos separados por comas: ")
lista = productos.split(",")

for productos in lista:
    print(productos.strip())
