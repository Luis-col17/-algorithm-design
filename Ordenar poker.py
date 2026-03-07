import random
palos = ["picas", "diamantes", "treboles", "corazones"]
numeros = [8, 3, 11, 1, 9, 5, 13, 2, 7, 10, 4, 12, 6]
orden_palos = {"treboles": 1, "picas": 2,  "corazones": 3, "diamantes": 4}

def crear_mazo(palos, numeros):
    mazo = []
    for i in range(len(palos)):
        for j in range(len(numeros)):
            mazo.append({"numero": numeros[j], "palo": palos[i]})

    return mazo


def ordenar_mazo(mazos):
    n = len(mazos)
    for i in range(1,n):
        j = i - 1
        key = mazos[i]
        key_numero = key["numero"]
        key_palo = orden_palos[key["palo"]]
        while j >= 0 and (key_palo < orden_palos[mazos[j]["palo"]] or (key_palo == orden_palos[mazos[j]["palo"]] and key_numero < mazos[j]["numero"])):
            mazos[j + 1] = mazos[j]
            j -= 1
        mazos[j + 1] = key
    return mazos


mazo_completo = crear_mazo(palos, numeros)
random.shuffle(mazo_completo)
print("Mazo sin ordenar: ", mazo_completo, "\n")
print("Mazo ordenado por número y palo: ", ordenar_mazo(mazo_completo))
# print("Mazo ordenado por número: ", ordenar_numero(mazo_completo), "\n")    
# print("Mazo ordenado por palo: ", ordenar_palo(mazo_completo))
