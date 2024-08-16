def promedio_notas(notas_estudiantes):
    promedios = {}
    for estudiante, calificaciones in notas_estudiantes:
        promedio = sum(calificaciones) / len(calificaciones)
        promedios[estudiante] = promedio
    return promedios

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
promedios = promedio_notas(notas_estudiantes)
print(promedios)
