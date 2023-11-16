import random

a = 20

lista = []

while a > 0:
    tal = random.randint(1,6)

    lista.append(tal)

    a = a - 1

b = 0

for i in lista:
    if i == 3:
        b = b + 1

print(lista)

print(b)

lista.pop(4)