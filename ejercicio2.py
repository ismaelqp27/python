nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

# 2. Guardamos la información en un diccionario
usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}
# 3. Mostramos el mensaje formateado
# Accedemos a los valores usando sus respectivas claves
print(f"\n{usuario['nombre']} tiene {usuario['edad']} años, "
      f"vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")