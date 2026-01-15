curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0

for asignatura, creditos in curso.items():
    print(asignatura, "tiene", creditos, "créditos")
    total_creditos = total_creditos + creditos

print("\nNúmero total de créditos del curso:", total_creditos)