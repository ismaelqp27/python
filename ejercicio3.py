primer_numero = int (input ("dime el numero que quieres dividir "))
segundo_numero = int (input ("dime el numero por el que vas a dividir al anterior "))
resultado = primer_numero / segundo_numero

if segundo_numero == 0:
    print ("error, no se puede doividir entre 0 ")
else:
    print ("el resultado es: " , resultado)