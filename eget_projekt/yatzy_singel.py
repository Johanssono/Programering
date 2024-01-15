import random

player = []
dice = []
antal = 5
saved = []


namn = input("Skriv namn på spelare: ")
player.append(namn)

svar = input("Vill du spela ett spel? j/n: ")

if svar == "j":
    antal = 0
    kast = 3
    while kast > 0:
        
        kasta = input("Vill du kasta tärningarna? j/n: ")
        
        while kasta == "j":
            while antal < 5:
                tärning = random.randrange(1, 7)
                dice.append(tärning)
                antal = antal + 1

            print(dice)

            save_dice = input("Vill du spara några tärningar? j/n: ")

            while save_dice == "j":
                print(dice)
                save = int(input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: "))
                for i in range(dice.len()-1, 0, -1):
                    if dice[i] == save:
                        saved.append(save)
                        dice.remove(save)
                '''
                for tal in dice:
                    if (tal == save):
                        saved.append(tal)
                        dice.remove(tal)
                '''
                print(dice)
                save_dice = input("Vill du spara några fler tärningar? j/n: ")


            print("sparade tärningarx: ", dice)
            
            remove_dice = input("Vill du ta bort några tärningar? j/n: ")

            if remove_dice == "j":
                delete = input("1, 2, 3, 4, 5 eller 6? ")
                for tal in dice:
                    if (tal == delete):
                        delete.remove(tal)

            print(dice)
            antal = len(dice)
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
