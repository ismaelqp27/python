sexo = input ("dime tu sexo de poniendo hombre o mujer: ")
nombre = input ("ingrese su nombre: ")
inicial = nombre [0] . lower()
if sexo == "M" and inicial > "n":
    print ("pertenece al grupo A")
elif sexo == "M" and inicial <= "n":
    print ("pertenece al grupo B")
elif sexo == "F" and inicial < "m":
    print ("pertenece al grupo A")
else:
    print ("pertenece al grupo B")