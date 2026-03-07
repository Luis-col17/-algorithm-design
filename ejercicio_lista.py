from datetime import datetime
import time

incio = datetime.now()

x = [3,7,53,2,7,1,4,6,1,7,4,26,]

def encontrar_numero(numero):
    for i in x:
        if i == numero:
            return True
    return False

nume = int(input("Encontrar numero: "))
if encontrar_numero(nume) == True:
    print("El número se encuentra en la lista.")
else:
    print("El número no se encuentra en la lista.")

def busqueda_binaria_iterativa(lista, objetivo):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio  # Objetivo encontrado
        elif lista[medio] < objetivo:
            izq = medio + 1  # Buscar en la mitad derecha
        else:
            der = medio - 1  # Buscar en la mitad izquierda  
    return -1  # No encontrado
fin = datetime.now()

tiempo= fin - incio
print("Tiempo de ejecución: ", tiempo)

# Prueba



# def donde_insertar(lista, objetivo):
#     izq = 0
#     der = len(lista) - 1
    
#     while izq <= der:
#         medio = (izq + der) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             izq = medio + 1
#         else:
#             der = medio - 1
            
#     return izq  # Devuelve el punto de inserción

# # Prueba
# ordenada = [0, 2, 4, 6]
# print(donde_insertar(ordenada, 3))  # Resultado: 2 (se inserta entre 2 y 4)
# print(donde_insertar(ordenada, 5))  # Resultado: 3 (se inserta entre 4 y 6)

# 5