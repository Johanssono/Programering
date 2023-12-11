import random

spelare = []
tärningar = []
sparade = []


svar = input("Vill du spela ett spel? j/n: ")

if svar == "j":
    namn = input("Skriv namn på spelare: ")
    spelare.append(namn)

else:
    print("ok, ha en bra dag")

kast = input("Vill du kasta tärningarna? j/n: ")

if kast == "j":
    tärning_1 = random.randrange(1, 7)
    tärningar.append(tärning_1)

    tärning_2 = random.randrange(1, 7)
    tärningar.append(tärning_2)
    
    tärning_3 = random.randrange(1, 7)
    tärningar.append(tärning_3)
    
    tärning_4 = random.randrange(1, 7)
    tärningar.append(tärning_4)

    tärning_5 = random.randrange(1, 7)
    tärningar.append(tärning_5)

else:
    print("ok, ha en bra dag")

print(tärningar)

spara = int(input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: "))

for tal in tärningar:
    if (tal == spara):
        sparade.append(tal)
        tärningar.remove(tal)

for antal in tärningar:
    tärning_1 = random.randrange(1, 7)
    tärningar.append(tärning_1)
    antal = antal - 1

print(tärningar)