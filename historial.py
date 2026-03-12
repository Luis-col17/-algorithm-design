mi_navegacion = [ "google.com", "uniminuto.edu", "Error 404: Campus Virtual", "github.com", "stackoverflow.com", "bwm.com", "python.org", "wikipedia.org", "twitter.com", "facebook.com" ]
def retroceder_pagina(navegacion, pasos):
    if pasos == -1:
        return "No hay mas pasos para retroceder"
    elif "Error 404" in navegacion[-1]:
        print_ejemplo = navegacion[-1]
        return "No se puede retroceder a esta pagina, es un error 404"
    elif pasos > len(navegacion):
        return "No se puede retroceder mas de lo que se ha navegado"
    else: 
        print("Pagina actual: ", navegacion[-1])
        navegacion.pop()
        return retroceder_pagina(navegacion, pasos - 1)


pasos_a_retroceder = 4
print(retroceder_pagina(mi_navegacion, pasos_a_retroceder))