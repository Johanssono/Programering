import random

player = []
dice = []
saved = []
antal = 5


namn = input("Skriv namn på spelare: ")
player.append(namn)


svar = input("Hej", namn, "Vill du spela ett spel? j/n: ")

if svar == "j":
    kast = input("Vill du kasta tärningarna? j/n: ")

    
    while kast == "j":
        while antal > 0:
            tärning_1 = random.randrange(1, 7)
            dice.append(tärning)
            antal = antal - 1
            print(dice)

            spara = int(input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: "))

            for tal in dice:
                if (tal == spara):
                    saved.append(tal)
                    dice.remove(tal)

            print(dice)
            antal = 5 - len(dice)
            kast = input("Vill du kasta tärningarna? j/n: ")

else print("hej då")

#tärning_2 = random.randrange(1, 7)
#dice.append(tärning_2)

#tärning_3 = random.randrange(1, 7)
#dice.append(tärning_3)

#tärning_4 = random.randrange(1, 7)
#dice.append(tärning_4)

#tärning_5 = random.randrange(1, 7)
#dice.append(tärning_5)
