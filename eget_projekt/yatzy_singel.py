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

                
                for i in range(len(dice) -1, -1, -1):
                    if dice[i] == save:
                        saved.append(save)
                        dice.remove(save)

                        '''
                        Denna for slinga kollar igenom listan "dice" och lägger in dem i 
                        listan "saved", men for slingan kollar igenom listan "dice" backlänges 
                        för att int ändra index-värdet hos objekten i listan och garantera att 
                        alla bjekt av samma värde tas bort oavsätt index
                        '''


                '''
                for tal in dice:
                    if (tal == save):
                        saved.append(tal)
                        dice.remove(tal)

                tidigare försök till att skapa en aoutomatiserad lista som tar bort och lägger in vald tärning
                '''
                print(dice)
                save_dice = input("Vill du spara några fler tärningar? j/n: ")

            print("sparade tärningar: ", saved)
            
            remove_dice = input("Vill du ta bort några tärningar? j/n: ")



            while remove_dice == "j":
                delete = input("1, 2, 3, 4, 5 eller 6? ")
                for tal in dice:
                    if (tal == delete):
                        delete.remove(tal)
                
                print("sparade tärningar: ", saved)
            
                remove_dice = input("Vill du ta bort några tärningar? j/n: ")

            dice = []

            dice.extend(saved)
            
            print(dice)
            antal = len(dice)
            kasta = input("Vill du kasta tärningarna? j/n: ")
            kast = kast - 1

            if kast > 0:
                saved = []

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
