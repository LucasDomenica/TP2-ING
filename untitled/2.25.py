def analizar_finanzas(**kwargs):
    balance = 0

    for valor in kwargs.values():
        balance += valor

    return balance

balance_final = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"El balance final es: {balance_final}")
