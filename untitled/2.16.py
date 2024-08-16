def crear_perfil(nombre, edad, email, **kwargs):

    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }

    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil

perfil_usuario = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza", profesion="Ingeniero")
print(perfil_usuario)
