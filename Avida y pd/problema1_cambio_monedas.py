def cambio_greedy(monto, denominaciones):
   #funcion que utiliza las monedas de mayor valor primero para dar el cambio
    denominaciones_ordenadas = sorted(denominaciones, reverse=True) #se deja en forma descendente para usar las monedas de mayor valor primero
    monedas_usadas = []

    for moneda in denominaciones_ordenadas: #se recorre la lista de denominaciones ordenada
        while monto >= moneda: #mientras el monto sea mayor o igual a la moneda actual, se sigue usando esa moneda
            monedas_usadas.append(moneda) #se guarda la moneda usada en la lista de monedas usadas
            monto -= moneda #se resta el valor de la moneda al monto restante

    return monedas_usadas


monto = 87500
denominaciones = [50000, 20000, 10000, 5000, 1000]
denominacion_Extra = [50000, 20000, 10000, 7000, 5000, 1000]

print("Cambio de monedas - Algoritmo Greedy")
print(f"  Monto a dar: ${monto}")
print(f"  Denominaciones disponibles: {denominaciones}")
print()

# --- Greedy ---
monedas_g = cambio_greedy(monto, denominaciones)
print("[ GREEDY ]")
print(f"  Monedas usadas: {monedas_g}")
print(f"  Total de monedas: {len(monedas_g)}")
print()

# --- Greedy con denominación extra ---
monedas_g = cambio_greedy(monto, denominacion_Extra)
print("[ GREEDY extra]")
print(f"  Monedas usadas: {monedas_g}")
print(f"  Total de monedas: {len(monedas_g)}")