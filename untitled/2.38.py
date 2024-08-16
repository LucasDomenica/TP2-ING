def actualizar_suscripcion(suscripciones, usuario, suscripcion, **kwargs):
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    if suscripcion not in suscripciones[usuario]:
        suscripciones[usuario].append(suscripcion)
    if 'auto_renovacion' in kwargs:
        print(f"Auto-renovación {'activada' if kwargs['auto_renovacion'] else 'desactivada'} para {usuario}.")

    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

estado_actualizado = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)

print(estado_actualizado)
