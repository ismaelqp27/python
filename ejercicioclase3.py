base = int(input("Dime el número base: "))
exponente = int(input("Dime el exponente: "))

resultado = 1

for i in range(exponente):
    resultado *= base

print("El resultado es: ", resultado)
