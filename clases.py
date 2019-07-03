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

