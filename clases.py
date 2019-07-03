class Ave:
    def __init__(self):
        print('Soy un nuevo objeto')


    def volar(self, volar = True):
        print('Vuela: ' + str(volar))


class Pinguino(Ave):
    def __init__(self):
        print('Objeto de la clase pinguino')


class Paloma(Ave):
    def __init__(self):
        print('Objeto de la clase paloma')


# Herencia múltiple
class Engendro(Pinguino, Paloma):
    pass

# Pinguino
objeto_pinguino = Pinguino()
objeto_pinguino.volar(False)

# Paloma
objeto_paloma = Paloma()
objeto_paloma.volar()

# Engendro
engendro = Engendro()
engendro.volar(False)

# Clases decoradoras


class Decorador(object):
    """Mi clase decoradora"""
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        print('Funcion ejecutada: ' + self.funcion.__name__)
        self.funcion(*args, **kwargs)


@Decorador
def resta(valor1, valor2):
    print(int(valor1) - int(valor2))


resta(2064, 2020)

