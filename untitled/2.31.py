def publicar(nombre_usuario, texto_publicacion, **kwargs):
    detalles_publicacion = {
        "usuario": nombre_usuario,
        "texto": texto_publicacion,
    }
    if "etiquetas" in kwargs:
        detalles_publicacion["etiquetas"] = kwargs["etiquetas"]
    for key, value in kwargs.items():
        if key != "etiquetas":
            detalles_publicacion[key] = value
    return detalles_publicacion

publicacion = publicar(
    "Juan",
    "Mi primer post!",
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica",
    likes=100
)
print(publicacion)
