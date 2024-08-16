def actualizar_inventario(inventario, ventas):
    if len(inventario) != len(ventas):
        raise ValueError("Las listas de inventario y ventas deben tener la misma longitud")


    inventario_actualizado = [inventario[i] - ventas[i] for i in range(len(inventario))]

    return inventario_actualizado


inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

inventario_actualizado = actualizar_inventario(inventario, ventas)
print(inventario_actualizado)
