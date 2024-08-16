def calcular_promedio(*args):

    
    if len(args) == 0:
        return 0
    promedio = sum(args) / len(args)
    return promedio

promedio = calcular_promedio(85, 90, 78, 92)
print(f"El promedio de las notas es: {promedio}")
