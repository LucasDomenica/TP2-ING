def libros_publicados_despues_de_2000(biblioteca):
    libros_modernos = []

    for titulo, info in biblioteca.items():

        if info["año"] > 2000:
            libros_modernos.append(titulo)
    return libros_modernos

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

libros = libros_publicados_despues_de_2000(biblioteca)
print("Libros publicados después del año 2000:", libros)
