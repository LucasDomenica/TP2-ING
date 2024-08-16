def empleados_con_salario_mayor(empleados, salario_minimo):
    empleados_filtrados = {}

    for id_empleado, info in empleados.items():
        nombre, edad, salario = info
        if salario > salario_minimo:
            empleados_filtrados[id_empleado] = info

    return empleados_filtrados

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

resultado = empleados_con_salario_mayor(empleados, 3000)
print(resultado)
