import random

player = []
dice = []
saved = []
antal = 5


namn = input("Skriv namn på spelare: ")
player.append(namn)

svar = input("Vill du spela ett spel? j/n: ")

if svar == "j":

    kast = 3
    while kast > 0:
        
        kasta = input("Vill du kasta tärningarna? j/n: ")
        
        while kasta == "j":
            while antal > 0:
                tärning = random.randrange(1, 7)
                dice.append(tärning)
                antal = antal - 1

            print(dice)

            spara = int(input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: "))

            for tal in dice:
                if (tal == spara):
                    saved.append(tal)
                else:
                    dice.remove(tal)

            print(saved)
            
            delete = int(input("Vill du ta bort några? 1, 2, 3, 4, 5 eller 6: "))

            for tal in saved:
                if (tal == delete):
                    delete.remove(tal)
                    delete.remove(tal)

            print(dice)
            antal = 5 - len(dice)
            kasta = input("Vill du kasta tärningarna? j/n: ")
            
        kast = kast - 1

else:
    print("hej då")

    #tärning_2 = random.randrange(1, 7)
    #dice.append(tärning_2)

    #tärning_3 = random.randrange(1, 7)
    #dice.append(tärning_3)

    #tärning_4 = random.randrange(1, 7)
    #dice.append(tärning_4)

    #tärning_5 = random.randrange(1, 7)
    #dice.append(tärning_5)
