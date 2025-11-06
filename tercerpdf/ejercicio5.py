numero = int (input("Dime tu edad: "))
ingresos = int (input("Dime tus ingresos mensuales: "))
if numero >= 16 and ingresos >= 1000:
    print("tienes que tributar")
else:
    print ("no tienes que tributar")