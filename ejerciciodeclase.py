saldo = float (1000)
##saldo = float (input ("dime cual es tu saldo: "))
##ingreso = float (input ("dime cuanto dinero quieres ingresar: "))
##reintegro = float (input ("dime cuanto dinero quieres sacar: "))
opcion = ""
while opcion != "4":
    print ("1. saldo")
    print ("2. ingreso")
    print ("3. reintegro")
    print ("4. salir")
    opcion = input ("¿que opcion quieres usar? ")
    
    if opcion == "3":
        print ("tu saldo actual es de: " , saldo , "€")
    if opcion == "2":
        ingresar = float ( input ("dime cuanto dinero quieres ingresar: "))
        total = saldo + ingresar 
        print ("tu saldo actual es de: " , total , "€")

    if opcion == "3":
        sacar = float ( input ("dime cuanto dinero quieres sacar: "))
        total = saldo - sacar
        print ("tu saldo actual es de: " , total , "€")
    else:
        print ("cipollo")

