edad = int (input ("cuantos años tiene el cliente "))
if edad < 4:    
    print ("entra gratis")
elif edad > 4 and edad < 18:
    print ("paga 5€")
else: 
    print ("paga 10€")