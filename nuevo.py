x="hola"
y="hola"


if x == y:
    print('son iguales en valor')

print(id(x), id(y))

if x is y:
    print('ok')
else:
    print('nok')

# print(str(None))
print((str(None)is None))
print(id(None))
