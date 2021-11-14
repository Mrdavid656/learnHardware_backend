
def create_user(data, UserProfile, Nivel):
    user = UserProfile()
    user.first_name = data.data['first_name']
    user.last_name = data.data['last_name']
    user.email = data.data['email'] if 'email' in data.data else ''
    user.username = data.data['username']
    user.set_password(data.data['password'])
    user.nivel = Nivel.objects.filter(id=1).first()
    user.puntos = data.data['puntos'] if 'puntos' in data.data else 0
    user.save()
    return user


def isUserLevelUp(args, models):
    if args['puntos'] > 0:
        usuario = models['UserProfile'].objects.filter(id=args['usuario']).first()
        usuario.puntos += args['puntos']
        nivel = models['Nivel'].objects.filter(id=usuario.nivel_id).first()
        if usuario.puntos >= nivel.limite_puntos:
            niveles = models['Nivel'].objects.all().order_by('id')
            usuario.nivel = niveles[int(nivel.nombre)]
            usuario.puntos = 0
            usuario.save()
            return True
        usuario.save()
