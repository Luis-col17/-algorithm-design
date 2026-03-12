import requests
def obtener_paises():
    url="https://restcountries.com/v3.1/region/europe"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        
        paises= []
        for i in respuesta.json():
            paises.append({
                "nombre": i['name']['common'].lower(),
                "googleMaps": i['maps']['googleMaps']
            })
        
        return sorted(paises, key=lambda x: x['nombre'])
    
    except Exception as e:
        print("Error al obtener los datos: ", e)
        return []

def seleccion_de_busqueda(PAISES, BUSQUEDA, tipo_busqueda):
    if tipo_busqueda == 1: #busqueda lineal
        for i in PAISES:
            if i['nombre'] == BUSQUEDA:
                return i['googleMaps']
        return "nada....."
    elif tipo_busqueda == 2: #busqueda binaria
        izquierda = 0
        derecha = len(PAISES) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = PAISES[medio]['nombre']
            if valor_medio == BUSQUEDA:
                return PAISES[medio]['googleMaps']
            elif valor_medio < BUSQUEDA:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return "nada....."
    
    else: 
        print("seleccione la opcion correcta")    
        
paises = obtener_paises()
Exit = False
while Exit == False:
    name_country = input("Ingrese el nombre del pais en ingles: ").lower()
    Selection = int(input("Seleccione el tipo de busqueda: \n1.Lineal \n2.Binaria \n: "))
    print("Nombre del pais", name_country ,"con siguiente link: ",seleccion_de_busqueda(paises, name_country, Selection))
    padlock = input("Desea salir? (s/n): ").lower()
    if padlock == "s":
        Exit = True
        print("Saliendo, ADIOS!")