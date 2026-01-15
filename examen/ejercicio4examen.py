while True:
    print("Menu de opciones:")
    print("1. Contar palabras de una frase")
    print("2. Mostrar las palabras de una frase en líneas distintas")
    print("3. Mostrar la frase con todas sus letras en mayúsculas")
    print("4. Salir del programa")

    opcion = input("Seleccione una opcion (Entre el 1 y el 4): ")

    if opcion == '1':
        frase = input("Ingrese una frase: ")
        palabras = frase.split()
        print ("Contador de palabras:", len(palabras))

    elif opcion == '2':
        frase = input("Ingrese una frase: ")
        palabras = frase.split()
        for palabra in palabras:
            print(palabra)

    elif opcion == '3':
        frase = input("Ingrese una frase: ")
        print(frase.upper())

    elif opcion == '4':
        print("Saliendo del programa...")
        break
     