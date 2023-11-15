import random

tal = random.randint(1, 6)

a = 10

lista = []

while a > 0:
    b = random.randint(1, 6)

    lista.append(b)

    a = a - 1

print(lista)

d = 0

for k in lista:
    if k == 3:
        d = d + 1

print(d)