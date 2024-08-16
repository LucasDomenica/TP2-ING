def producto_mas_caro(productos):
    producto_caro = max(productos, key=lambda producto: producto[1])
    return producto_caro

productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

resultado = producto_mas_caro(productos)
print("El producto más caro es:", resultado)