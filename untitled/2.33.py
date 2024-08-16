def hacer_reserva(reservas, fecha, nombre, habitacion, precio):
    if fecha in reservas:
        for reserva in reservas[fecha]:
            if reserva[1] == habitacion:
                return f"Error: La habitación {habitacion} ya está reservada el {fecha}."
        reservas[fecha].append((nombre, habitacion, precio))
    else:
        reservas[fecha] = [(nombre, habitacion, precio)]
    return f"Reserva confirmada para {nombre} en la habitación {habitacion} el {fecha}."

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
print(hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 150))
print(hacer_reserva(reservas, "2024-08-15", "Carlos", 103, 150))
print(reservas)
