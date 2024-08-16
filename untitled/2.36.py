def actualizar_inventario(tienda, inventario, **kwargs):
    if tienda in inventario:
        for producto, cantidad in kwargs.items():
            if producto in inventario[tienda]:
                inventario[tienda][producto] += cantidad
            else:
                inventario[tienda][producto] = cantidad
    else:
        inventario[tienda] = kwargs

    return inventario
inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
inventario_actualizado = actualizar_inventario("Tienda A", inventario, producto_1=10, producto_2=-5)
print(inventario_actualizado)
