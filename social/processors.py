from .models import Link

#GENERAMOS UN DICCIONARIO CON LAS REDES SOCIALES CON SU CLAVE Y SUS VALORES (URL) Y LO DEVOLVEMOS
def prueba_dict(request):
    ctx = {}
    links = Link.objects.all()
    
    for link in links:
        ctx[link.key] = link.url
    
    return ctx