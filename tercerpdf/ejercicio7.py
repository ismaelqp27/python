renta = input ("digamme su renta anual en euros: ")
if renta < "10000":
    print ("su tipo impositivo es del 5%")
elif renta >= "10000" and renta <= "20000":
    print ("su tipo impositivo es del 15%")
elif renta > "20000":
    print ("su tipo impositivo es del 20%")
elif renta > "35000":
    print ("su tipo impositivo es del 30%")
else:
    print ("su tipo impositivo es del 45%")