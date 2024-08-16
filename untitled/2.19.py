def analizar_resultados(resultados):
    total_goles_anotados = 0
    total_goles_recibidos = 0

    for goles_anotados, goles_recibidos in resultados.values():
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos

    return total_goles_anotados, total_goles_recibidos

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

goles_anotados, goles_recibidos = analizar_resultados(resultados)
print(f"Total de goles anotados: {goles_anotados}")
print(f"Total de goles recibidos: {goles_recibidos}")
