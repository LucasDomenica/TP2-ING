def ventas (ventas_mensuales):
    total_ventas = sum(ventas_mensuales)
    prom_ventas = total_ventas / len(ventas_mensuales)
    indice_mayor_venta = ventas_mensuales.index(max(ventas_mensuales))

# Devolver el número del mes (1 a 12) con la mayor venta
    return indice_mayor_venta + 1, total_ventas, prom_ventas

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

mes, total, promedio = ventas(ventas_mensuales)
print("el mes con mayor venta es: ",mes)
print("El promedio de ventas es: ", promedio)
print("El total de ventas es: ", total)


