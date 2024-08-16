def filtrar_rutas(rutas, distancias_max):
    rutas_validas = []
    for ruta, distancia_max in zip(rutas, distancias_max):
        if ruta[2] <= distancia_max:
            rutas_validas.append(ruta)
    return rutas_validas

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]
rutas_validas = filtrar_rutas(rutas, distancias_max)

print(rutas_validas)
