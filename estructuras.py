
# numeros = [0,1,2,3,4,5,6,7,8,9,10]
# print(numeros[1])

# slices, empezando del cero al seis
# print(numeros[0:6])

# empezando del cero al x
# print(numeros[0:100])

# empezando en el indice 2
# print(numeros[2:])

# diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
# print (diccionario['nombre'])


# l = list(range(100))
# l = [str(i) for i in l]
# print(l)

# algo = [None] * 10

# l = (str(i) for i in range(10))
# print(type(l))
# print(l)
# for x in l:
    # print(x)

for x in range(9_999_999_999):
    print(x)
    break

dest = [None] * 3
nombres = ['enzo', 'eduardo', 'ernesto']
#for nombre in nombres:
#     dest.append(nombre)

# print(dest)

#for i in range(len(dest)):
#    dest[i] = (i, nombres[i])

# print(dest[0][1])

for i, n in enumerate(nombres):
    dest[i] = (i, n)
    print(dest)

