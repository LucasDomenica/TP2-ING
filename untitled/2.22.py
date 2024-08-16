
def precio(paquetes):
    precios_totales = {}
    for destino, precio, duracion in paquetes:
        precio_total = precio * duracion
        precios_totales[destino] = precio_total
    return precios_totales

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

resultado = precio(paquetes)
print(resultado)
