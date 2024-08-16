def simular_mercado(precios_diarios, operaciones):
    saldo = 0
    acciones = 0
    compra_precio = 0

    for operacion, dia in operaciones:
        if operacion == "compra":

            if dia < len(precios_diarios):
                compra_precio = precios_diarios[dia]
                acciones += 1
                saldo -= compra_precio
        elif operacion == "venta":

            if dia < len(precios_diarios) and acciones > 0:
                venta_precio = precios_diarios[dia]
                saldo += venta_precio
                acciones -= 1

    beneficio_total = saldo + (acciones * precios_diarios[-1])
    return beneficio_total
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
resultado = simular_mercado(precios_diarios, operaciones)

print(f"Beneficio o pérdida total: {resultado}")
