def ordenar_por_puntuacion(puntuaciones):

    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
puntuaciones_ordenadas = ordenar_por_puntuacion(puntuaciones)
print(puntuaciones_ordenadas)
