def knapsack(proyectos, presupuesto):
    n = len(proyectos)
    W = presupuesto

    # Tabla dp: filas = proyectos (+ fila 0 vacía), columnas = presupuesto
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Llenar la tabla
    for i in range(1, n + 1):
        costo = proyectos[i - 1]['costo']
        roi   = proyectos[i - 1]['roi']
        for w in range(W + 1):
            # opcion 1: realizar el proyecto i-ésimo (si no lo hacemos, el valor es el mismo que sin este proyecto), coge el valor en diagonal izquierda a la fila anterior
            dp[i][w] = dp[i - 1][w]
            # Opción 2: incluirlo (solo si cabe en el presupuesto), coge el valor del proyecto + el valor máximo acumulado con el presupuesto restante (mirando en la fila anterior)
            if costo <= w:
                con_proyecto = roi + dp[i - 1][w - costo]
                if con_proyecto > dp[i][w]:
                    dp[i][w] = con_proyecto

    return dp


def backtracking(dp, proyectos, presupuesto):
    seleccionados = []
    n = len(proyectos)
    w = presupuesto

    for i in range(n, 0, -1):#recorre la tabla dp desde la última fila (todos los proyectos considerados) hacia arriba, y desde el presupuesto total hacia abajo
        if dp[i][w] != dp[i - 1][w]: ## Si no cambia, no se toma; si cambia, se toma y se descuenta el costo
            seleccionados.append(proyectos[i - 1])
            w -= proyectos[i - 1]['costo']#se resta el costo del proyecto seleccionado

    return seleccionados


def imprimir_tabla(dp, proyectos, presupuesto):
    n = len(proyectos)
    print("  Tabla dp (ROI máximo acumulable):")
    # Encabezado
    encabezado = f"  {'Item':<15}"
    for w in range(0, presupuesto + 1):
        encabezado += f"  ${w}M"
    print(encabezado)
    print("  " + "-" * (15 + (presupuesto + 1) * 5))

    # Fila vacía (sin proyectos)
    fila = f"  {'(vacío)':<15}"
    for w in range(presupuesto + 1):
        fila += f"  {dp[0][w]:3d}"
    print(fila)

    # Filas de proyectos
    for i in range(1, n + 1):
        nombre = proyectos[i - 1]['nombre'] #saca el nombre del proyecto para mostrarlo en la tabla
        fila = f"  {nombre:<15}"
        for w in range(presupuesto + 1):
            fila += f"  {dp[i][w]:3d}" #añade el valor del ROI acumulado para cada presupuesto en la fila correspondiente al proyecto
        print(fila)
    print()



proyectos = [
    {'nombre': 'HealthTech',  'roi': 7, 'costo': 3},
    {'nombre': 'AI Startup',  'roi': 9, 'costo': 5},
    {'nombre': 'GreenTech',   'roi': 4, 'costo': 2},
    {'nombre': 'Fintech',     'roi': 6, 'costo': 4},
]
presupuesto = 10  


print("  CARTERA ÓPTIMA DE INVERSIÓN — Knapsack \n")

print(f"\n  Presupuesto disponible: ${presupuesto}M")
print("\n  Proyectos disponibles:")
print(f"  {'Proyecto':<15} {'ROI':>6} {'Costo':>7}") #nota el :<15 para alinear a la izquierda con un ancho de 15 caracteres, y el :>6 y :>7 para alinear a la derecha con anchos de 6 y 7 caracteres respectivamente
print("  " + "-" * 30)
for p in proyectos: #recorre la lista de proyectos y muestra su nombre, ROI y costo formateados en columnas
    print(f"  {p['nombre']:<15} ${p['roi']:>4}M  ${p['costo']:>4}M")

print()

# Resolver con PD
tabla = knapsack(proyectos, presupuesto)

# Mostrar tabla dp
imprimir_tabla(tabla, proyectos, presupuesto)

# Resultado óptimo
roi_maximo = tabla[len(proyectos)][presupuesto]
print(f"  ROI máximo posible: ${roi_maximo}M") #el ROI máximo se encuentra en la última fila (todos los proyectos considerados) y la columna del presupuesto total

# Backtracking: que proyectos se eligieron para lograr ese ROI máximo
elegidos = backtracking(tabla, proyectos, presupuesto)
costo_total = sum(p['costo'] for p in elegidos) #suma el costo de los proyectos elegidos para mostrar cuánto del presupuesto se usó
roi_total   = sum(p['roi']   for p in elegidos) #suma el ROI de los proyectos elegidos para mostrar el ROI total obtenido con la cartera óptima

print(f"\n  Cartera óptima (backtracking):")
for p in elegidos: #recorre la lista de proyectos elegidos y muestra su nombre, ROI y costo formateados en columnas
    print(f"    ✓ {p['nombre']} — ROI: ${p['roi']}M, Costo: ${p['costo']}M")
print(f"\n  Costo total:  ${costo_total}M / ${presupuesto}M usados")
print(f"  ROI total:    ${roi_total}M")

# print()
# print("ANÁLISIS DE COMPLEJIDAD:")
# print(f"  Tiempo:  O(n × W) = O({len(proyectos)} × {presupuesto}) = O({len(proyectos)*presupuesto})")
# print(f"  Espacio: O(n × W) → optimizable a O(W)")
# print()
# print("APLICACIÓN REAL:")
# print("  Facebook Ads usa variantes del Knapsack para asignar")
# print("  presupuesto publicitario entre campañas y maximizar")
# print("  impresiones dentro del presupuesto del anunciante.")
# print("=" * 60)
