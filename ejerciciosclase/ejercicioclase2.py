suma = 0
mayor = 0
menor= 0
for i in range(1, 6):
    num = int(input("Dime un número: "))
    suma += num
    if mayor < num:
        mayor = num
    if menor > num:
        menor = num
print ("La suma total es: ", suma)
print ("El número mayor es: ", mayor)
print ("el numero menor es: " , menor)