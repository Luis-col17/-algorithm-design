def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Crear la tabla dp con dimensiones (m+1) x (n+1), inicializada toda la tabla a 0 
    dp = [[0] * (n + 1) for _ in range(m + 1)] #

    for i in range(1, m + 1): #empezamos desde 1 porque la fila y columna 0 representan el caso base de cadenas vacías
        for j in range(1, n + 1): #recorremos cada celda de la tabla dp para llenarla según las reglas del LCS
            
            if X[i - 1] == Y[j - 1]: #si la letra es igual en ambas versiones (coinciden), entonces la LCS se extiende en 1 
                
                # Los caracteres coinciden: extendemos la LCS anterior en 1 
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # No coinciden: tomamos el mejor de ignorar uno u otro, tomamos el mismo valor que el de arriba o el de la izquierda, dependiendo cuál sea mayor
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

#funcion para reconstruir la LCS a partir de la tabla dp, haciendo backtracking desde la esquina inferior derecha hasta la esquina superior izquierda
def backtracking_lcs(dp, X, Y):
    lcs_str = [] #creamos una lista para ir guardando los caracteres que forman la LCS mientras hacemos el backtracking
    i, j = len(X), len(Y) 
    
    while i > 0 and j > 0: #mientras no hayamos llegado a la fila o columna 0, seguimos haciendo backtracking
        #---------variables para facilitar la lectura del código---------
        xx=X[i - 1] #extra la letra actual de x 
        yy=Y[j - 1] #extra la letra actual de y
        valor_izquierda = dp[i][j - 1] #identificamos el valor de la celda de la izquierda
        valor_arriba = dp[i - 1][j] #identificamos el valor de la celda de arriba
        valor_actual = dp[i][j] #identificamos el valor de la celda actual
        #--------------------------------------------------------------
        if X[i - 1] == Y[j - 1]: #si los caracteres coinciden, entonces ese carácter forma parte de la LCS.
            # Este carácter forma parte de la LCS
            lcs_str.append(X[i - 1])
            #retrocedemos en ambas direcciones porque ese carácter ya fue incluido en la LCS
            i -= 1 
            j -= 1
        
        elif dp[i - 1][j] > dp[i][j - 1]: #si el valor de la celda de arriba es mayor que el de la izquierda, eso significa que la LCS se extendía más al ignorar el carácter de Y, entonces retrocedemos hacia arriba
            # Viene de arriba
            i -= 1
        else:
            # Viene de la izquierda
            #retrocedemos hacia la izquierda porque el valor de la celda de la izquierda es mayor o igual al de arriba, lo que significa que la LCS se extendía más al ignorar el carácter de X
            j -= 1

    lcs_str.reverse()  # las letras seleccionadas se agregaron en orden inverso, por lo que las invertimos para obtener la LCS correcta
    return ''.join(lcs_str)


def imprimir_tabla(dp, X, Y):
    m, n = len(X), len(Y)
    print("  Tabla dp completa:")
    print()

    # Encabezado con caracteres de Y
    enc = f"  {'':>5}  {'ε':>3}"
    for c in Y: #reccorremos los caracteres de Y para imprimirlos en el encabezado de la tabla
        enc += f"  {c:>2}" #imprime cada carácter de Y con un espacio de 2 caracteres a la derecha para alinear con la tabla
    print(enc)
    print("  " + "-" * (6 + (n + 1) * 4)) #linea separadora

    # Fila inicial (sin caracteres de X)
    fila = f"  {'ε':>5}  "
    for j in range(n + 1): #imprime la fila inicial de la tabla dp
        fila += f" {dp[0][j]:>2} "
    print(fila)

    # Filas con caracteres de X
    for i in range(1, m + 1): #imprime cada fila de la tabla dp, comenzando desde la fila 1 porque la fila 0 ya fue utilizada
        fila = f"  {X[i-1]:>5}  "
        for j in range(n + 1):#imprime cada celda de la fila actual, junto con el carácter correspondiente de X al inicio de la fila
            fila += f" {dp[i][j]:>2} "
        print(fila)
    print()


# def analizar_diferencias(X, Y, lcs_resultado):
#     """
#     Interpreta qué significa la LCS en términos de versionado.
#     Muestra qué se mantuvo, qué se agregó y qué se eliminó.
#     """
#     print("  Interpretación en control de versiones:")
#     print()
#     # Caracteres que se mantuvieron (están en la LCS)
#     comunes = set(lcs_resultado)
#     solo_v1 = [c for c in X if c not in Y]
#     solo_v2 = [c for c in Y if c not in X]

#     print(f"  LCS (líneas en común): '{lcs_resultado}'")
#     print(f"  → Estas letras/partes sobrevivieron entre versiones.")
#     print()
#     print(f"  En v1 pero no en v2: {[c for c in X if c not in lcs_resultado]}")
#     print(f"  → Estas partes fueron ELIMINADAS al pasar a v2.")
#     print()
#     print(f"  En v2 pero no en v1: {[c for c in Y if c not in lcs_resultado]}")
#     print(f"  → Estas partes fueron AGREGADAS en v2.")



v1 = "DEPLOY-PROD-DB-01"
v2 = "DEVELOP-DEBUG-01"

print("=" * 60)
print("  CONTROL DE VERSIONES — LCS")
print("=" * 60)
print(f"\n  v1: \"{v1}\"")
print(f"  v2: \"{v2}\"")
print()

# Calcular LCS
tabla = lcs(v1, v2)

# Mostrar tabla
imprimir_tabla(tabla, v1, v2)

# Resultado
longitud = tabla[len(v1)][len(v2)] #se toma el valor de la esquina inferior derecha de la tabla dp, que representa la longitud de la LCS entre v1 y v2
subsecuencia = backtracking_lcs(tabla, v1, v2)#se imprime el LCS encontrada haciendo backtracking a partir de la tabla dp

print(f"  Longitud de la LCS: {longitud}")
print(f"  LCS encontrada:     \"{subsecuencia}\"") 
print()


