nota1 = float(input("dime tu nota del primer examen: "))
nota2 = float(input("dime tu nota del segundo examen:"))
cuenta = (nota1 + nota2) /2
if nota1 <4 and nota2 <4:
    print ("tiene que recuperar ambos examenes")
elif nota1 <4:
    print ("tiene que recuperar solamente el primer examen")
elif nota2 <4:
    print ("tiene que recuperar solamente el segundo examen")
elif cuenta >=5:
    print ("la media da aprobada")
else:
    print ("la media da suspenso aunque las notas que has sacado sirven para hacer media")