print('Bienvenido')

try:
    print(1 / 0)

except TypeError:
    print('Error en tipo de dato')
except NameError:
    print('Variable no existe')
except ZeroDivisionError:
    print('No se puede dividir por cero')
else:
    print('No existe error')

print('Adios')
