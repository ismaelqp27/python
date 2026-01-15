divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa_usuario = input("Introduce el nombre de una divisa (Euro, Dollar o Yen): ").title()

simbolo = divisas.get(divisa_usuario)

if simbolo:
    print(f"El símbolo de {divisa_usuario} es: {simbolo}")
else:
    print("Error: La divisa no está en el diccionario.")