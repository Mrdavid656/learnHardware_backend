from juego.api import LogrosSerializer
from juego.models import UserLogros, Logros


def logrosGanados(historial, usuario):
    logros = []
    if len(historial) <= 1:
        logro = Logros.objects.filter(razon=Logros.FIRST_GAME_PLAYED).first()
        logros.append(logro)
    serializer = LogrosSerializer(logros, many=True)
    for logro in serializer.data:
        UserLogros.objects.create(usuario_id=usuario, logro_id=logro['id'])
    return serializer.data
