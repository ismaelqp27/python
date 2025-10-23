cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))
capital = cantidad * (1 + interes / 100) ** años
print("El capital final después de" + str(años) + " años es:", + str (capital, 2))
