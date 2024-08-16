def calcular_promedio_general(estudiantes):
    promedios = {}

    for estudiante_id, materias in estudiantes.items():
        suma_total = 0
        cantidad_calificaciones = 0

        for materia, calificaciones in materias.items():
            suma_total += sum(calificaciones)
            cantidad_calificaciones += len(calificaciones)

        promedio_general = suma_total / cantidad_calificaciones
        promedios[estudiante_id] = promedio_general

    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)

    return ranking
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = calcular_promedio_general(estudiantes)
print("Ranking de estudiantes basado en el promedio general:")
for estudiante_id, promedio in ranking:
    print(f"Estudiante ID {estudiante_id}: Promedio general = {promedio:.2f}")
