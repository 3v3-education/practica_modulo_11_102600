from .models import Mensaje, Autor

def mensajes_no_leidos(request):
    cantidad = 0

    if request.user.is_authenticated:

        try:
            autor_actual = Autor.objects.get(usuario=request.user)

            cantidad = Mensaje.objects.filter(destinatario=autor_actual, visto=False).count()
        except Autor.DoesNotExist:
            cantidad = 0

    return {'mensajes_no_leidos': cantidad}


