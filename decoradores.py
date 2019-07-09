# El nombre de la funcion es el nombre del decorador y recibe la funcion que decora (print_text).


def decor(func):
    def wrap():
        print("="*12)
        func()
        print("="*12)
    return wrap


@decor
def print_text():
    print("Hola Mundo!!!")

print_text()

loggeado = False


def admin(f):
    def comprobar(*args):
        if loggeado:
            f(*args)
        else:
            print('No tiene permisos para ejecutar la funcion: ' + f.__name__)
    return comprobar


def decorador(funcion):
    def funcion_decorada(*args):
        print('nombre de la funcion decorada: ' + funcion.__name__)
        funcion(*args)
    return funcion_decorada


@admin  # decorador
# @decorador
def resta(valor1, valor2):
    valor_resta = int(valor1) - int(valor2)
    print(valor_resta)


resta(2064, 1985)
