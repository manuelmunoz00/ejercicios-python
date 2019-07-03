import this


def foo(arg1, arg2):
    print(arg1, arg2)


def foo2(*, nombre, apellido_paterno, rut, apellido_materno):
    print(nombre, apellido_paterno, apellido_materno, rut)


def foo3(nombre, apellido_paterno, *, rut, apellido_materno):
    print(nombre, apellido_paterno, apellido_materno, rut)


def foo4(nombre, apellido_paterno, rut=None, apellido_materno=None):
    print(nombre, apellido_paterno, apellido_materno, rut)


foo('caca', 'poto')
foo(arg1='poto1', arg2='caca2')

foo2(nombre='Manuel', apellido_materno='Ayala', rut='16006363-7', apellido_paterno='Muñoz')

foo3('Manuel', 'Muñoz', rut='1-9', apellido_materno='algo')

foo4('Manuel', 'Muñoz')

real = 0.56
print(type(real))
print(7 % 3)

cadena = 'cadena'
cadena2 = """
asd
asdasd
asdsad
"""

print(cadena2)

cad = cadena * 3
print(cad + ' algo')
booleano = True
booleano2 = False

bAnd = True and False
print(bAnd)
booleano3 = not booleano2
print(booleano3)

# Listas
lista = ["uno", 2, "tres", True]
lista[0] = 1
print(lista[0])

lista2 = lista[0:3]
print(lista2)

lista3 = lista[-1]
print(lista3)
print(type(lista))

# tuplas
tupla = (1, True, "Hola")
print(type(tupla))
# tupla[0] = "Hola"
print(tupla)

# Diccionarios (sin indices)
diccionario = {'nombre': 'Manuel', 'apellido_paterno': 'Muñoz', 'apellido_materno': 'Ayala', 'notas': [1, 2, 3]}
print(diccionario['notas'])

# operadores relacionales
v = 6
b = 6
c = v == b
d = v != b
meq = v > b
maq = v < b
print(c)
print(d)
print(meq)
print(maq)

# comparando cadenas
c1 = 'Hola'
c2 = 'Hola'
c3 = c1 == c2
print(c3)

edad = input()
if int(edad) >= 18 < 65:
    print('Eres mayor de edad y solo adulto')
elif int(edad) >= 18 >= 65:
    print('Eres mayor de edad y adulto mayor')
else:
    print('No eres mayor de edad')
print('Esto se ejecuta siempre')

while int(edad) < 18:
    print(edad)
    edad = int(edad) + 1

for x in lista:
    print(x)


class Animal():
    pass


class Perro(Animal):
    pass


class Perro:
    def __init__(self):
        self.animal = Animal()


class Perro:
    def __init__(self, animal):
        self.animal = animal


