def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        configuraciones = [kwargs]
        perfiles[usuario] = configuraciones

    return perfiles

usuarios = ["Ana", "Luis", "María"]
configuraciones = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

print(configuraciones)
