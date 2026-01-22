entrada = input("Introduce las palabras (español:inglés) separadas por comas: ")

diccionario = {}
lista_parejas = entrada.split(',')

for pareja in lista_parejas:
    datos = pareja.split(':')
    esp = datos[0].strip()
    ing = datos[1].strip()
    diccionario[esp] = ing

frase = input("\nIntroduce una frase en español: ")
palabras_frase = frase.split()

print("\nTraducción:")

for p in palabras_frase:
    if p in diccionario:
        print(diccionario[p], end=" ")
    else:
        print(p, end=" ")