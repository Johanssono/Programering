import random

player = []
dice = []
antal = 5
saved = []
table = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor", "Par", "Två Par", "tretal", "Fyrtal", "Kåk", "Liten stege", "Stor Stege", "Chans", "Yatzy"]
choices = []
 = []
poäng_ettor = []
poäng_tvåor = []
poäng_treor = []
poäng_fyror = []
poäng_femmor = []
poäng_sexor = []

namn = input("Skriv namn på spelare: ")
player.append(namn)

svar = input("Vill du spela ett spel? j/n: ")

if svar == "j":

    while svar == "j":
        antal = 0
        throw = 3

        while throw > 0:
            
            kasta = input("Vill du kasta tärningarna? j/n: ")
            
            while kasta == "j":
                while antal < 5:
                    tärning = random.randrange(1, 7)
                    dice.append(tärning)
                    antal = antal + 1

                if throw > 1:
                
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
                    throw = throw - 1

                    saved = []
                    kasta = input("Vill du kasta tärningarna? j/n: ")
                
                else:
                    throw = throw - 1
                    dice.sort()
                    print(dice)
                    print(table)
                    print()
                    kasta = "n"
                    

    #En lista med alla olika poängalternativ,
    #koden ska kolla listan med tärningar och sedan utesluta dalternativ från listan med poäng alternativ.
    #Detta genom att kolla vilka slags tärningar som listan med resulterande tärningar inehåller.

    #sedan ska programet visa dessa utvalda alternativ för spelaren och låta spelaren välja ett av alternativen
    #Om programmet bedömer att det inte finns några alternativ som faller samman med tärningarna,
    #ska programmet föra fram en lista med de återstående alternativen och låta spelaren stryka ett alternativ.

    #När ett alternativ är valt eller struket, ska listan ta bort detta alternativ och spara det i den slutgiltiga listan.
    #Sedan ska spelaren presenteras med den slutgiltiga listan och summan av poängen.

        for siffra in dice:
            if siffra == 1:
                for alternativ in table:
                    if alternativ == "Ettor":
                        if "1. Ettor" in choices:
                            pass
                        else:
                            choices.append("1. Ettor")

            elif siffra == 2:
                for alternativ in table:
                    if alternativ == "Tvåor":
                        if "2. Tvåo" in choices:
                            pass
                        else:
                            choices.append("2. Tvåor")
            
            elif siffra == 3:
                for alternativ in table:
                    if alternativ == "Treor":
                        if "3. Treor" in choices:
                            pass
                        else:
                            choices.append("3. Treor")
            
            elif siffra == 4:
                for alternativ in table:
                    if alternativ == "Fyror":
                        if "4. Fyror" in choices:
                            pass
                        else:
                            choices.append("4. Fyror")
            
            elif siffra == 5:
                for alternativ in table:
                    if alternativ == "Femmor":
                        if "5. Femor" in choices:
                            pass
                        else:
                            choices.append("5. Femor")
            
            elif siffra == 6:
                for alternativ in table:
                    if alternativ == "Sexor":
                        if "6. Sexor" in choices:
                            pass
                        else:
                            choices.append("6. Sexor")

        dice = [1, 2, 2, 5, 5]
        print(dice)

        ettor = dice.count(1)
        tvåor = dice.count(2)
        treor = dice.count(3)
        fyror = dice.count(4)
        femmor = dice.count(5)
        sexor = dice.count(6)
        
        if ettor > 1:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 1:
                                par.append(1)
                                dice.remove(1)
        if tvåor > 2:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 2:
                                par.append(2)
                                dice.remove(2)
        if treor > 3:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 3:
                                par.append(3)
                                dice.remove(3)
        if fyror > 4:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 4:
                                par.append(4)
                                dice.remove(4)
        if femmor > 5:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 5:
                                par.append(5)
                                dice.remove(5)
        if sexor > 6:
            for i in range(len(dice) -1, -1, -1):
                            if dice[i] == 6:
                                par.append(6)
                                dice.remove(6)
        
        if len(par) == 2:
            for alternativ in table:
                    if alternativ == "par":
                        if "7. par" in choices:
                            pass
                        else:
                            choices.append("7. par")
        elif len(par) == 4:
            ettor_1 = dice.count(1)
            tvåor_1 = dice.count(2)
            treor_1 = dice.count(3)
            fyror_1 = dice.count(4)
            femmor_1 = dice.count(5)
            sexor_1 = dice.count(6)
            if ettor_1 = 2 or tvåor_1 = 2 or treor_1 = 2 or fyror_1 = 2 or femmor_1 = 2 or sexor_1 = 2:
                for alternativ in table:
                        if alternativ == "tvåpar":
                            if "8. tvåpar" in choices:
                                pass
                            else:
                                choices.append("8. tvåpar")
            elif ettor_1 = 4 or tvåor_1 = 4 or treor_1 = 4 or fyror_1 = 4 or femmor_1 = 4 or sexor_1 = 4:
                for alternativ in table:
                        if alternativ == "fyrtal":
                            if "10. fyrtal" in choices:
                                pass
                            else:
                                choices.inset("10. fyrtal")


        elif len(par) == 3:
            for alternativ in table:
                    if alternativ == "tretal":
                        if "9. tretal" in choices:
                            pass
                        elif "10. fyrtal" in choices:
                                choices.insert(9, "9. tretal")
                        else:
                            choices.append("9. tretal")





        elif len(par) == 5:
            ettor_2 = dice.count(1)
            tvåor_2 = dice.count(2)
            treor_2 = dice.count(3)
            fyror_2 = dice.count(4)
            femmor_2 = dice.count(5)
            sexor_2 = dice.count(6)
            if ettor_2 > 1 and ettor_2 < 4 or tvåor_2 > 1 and tvåor_2 < 4 or treor_2 > 1 and treor_2 < 4 or fyror_2 > 1 and fyror_2 < 4 or femmor_2 > 1 and femmor_2 < 4 or sexor_2 > 1 and sexor_2 < 4:
                for alternativ in table:
                        if alternativ == "kåk":
                            if "11. kåk" in choices:
                                pass
                            else:
                                choices.append("11. kåk")
            elif ettor_2 = 5 or tvåor_2 = 5 or treor_2 = 5 or fyror_2 = 5 or femmor_2 = 5 or sexor_2 = 5:
                for alternativ in table:
                        if alternativ == "yatzy":
                            if "15. yatzy" in choices:
                                pass
                            else:
                                choices.inset("15. yatzy")
"""
        b = 0
        c = 0
        a = dice[0]
        k = dice.index(a)

        for g in dice:
            if g == a:
                b = b + 1

                ##Blir en evighetsloop
        # hitta ett stort par
        # leta efter 6 minst 2 st
        dice.count(6)

        

        while k < 5:
            while b == 1:

                ##Blir en eveghetsloop
        
                b = 0
                a = dice[k + 1]
                k = dice.index(a)
                for g in dice:
                    if g == a:
                        b = b + 1

            if b == 2:
                while k < 5:    
                    while c < 2:

                        #fungerar om det finns en siffra mellan nr 2
                        k = dice.index(a, a + 1)
                        #till exempel om man ändrar om listan från 1, 2, 2, 5, 5 till 1, 2, 5, 2, 5

                        a = dice[k + 1]
                        k = dice.index(a)

                        if dice[4]:
                            for g in dice:
                                if g == a:
                                    c = c + 1            

"""
"""
while c < 2:
    d = index(3)
    if a == d:
        a = index(4)
    elif a != d:
        a = index 
"""
"""

            if b == 3:
                while k < 5:    
                    while c < 2:
                        a = dice.index(a) + 1
                        for g in dice:
                            if g == a:
                                c = c + 1


        if b == 2 or c == 3:
            if "7. par" in choices:
                pass
            else:
                choices.append("7. par")

        elif b == 2 and c == 2:
            if "8. tvåpar" in choices:
                pass
            else:
                choices.append("8. tvåpar")
        
        elif b == 3 or c == 3:
            if "9. tretal" in choices:
                pass
            else:
                choices.append("9. tretal")

        elif b == 4 or c == 4:
            if "10. fyrtal" in choices:
                pass
            else:
                choices.append("10. fyrtal")
        
        elif b == 2 and c == 3 or b == 3 and c == 2:
            if "11. kåk" in choices:
                pass
            else:
                choices.append("11. kåk")
"""

                    
        

        print(choices)

        sattsning = input("Skriv siffran på alternativet du önskar välja: ")

        if sattsning == "1":
            table.remove("Ettor")
            for etta in dice:
                if etta == 1:
                    poäng_ettor.append(1)
            poäng_ettor = sum(poäng_ettor)

        elif sattsning == "2":
            table.remove(Tvåor)
            for tvåa in dice:
                if tvåa == 2:
                    poäng_tvåor.append(2)
            poäng_tvåor = sum(poäng_tvåor)

        elif sattsning == "3":
            table.remove(Treor)
            for tvåa in dice:
                if etta == 3:
                    poäng_tvåor.append(3)
            poäng_treor = sum(poäng_treor)

        elif sattsning == "4":
            table.remove(Fyror)
            for tvåa in dice:
                if etta == 4:
                    poäng_tvåor.append(4)
            poäng_fyror = sum(poäng_fyror)

        elif sattsning == "5":
            table.remove(Femmor)
            for tvåa in dice:
                if etta == 5:
                    poäng_tvåor.append(5)
            poäng_femmor = sum(poäng_femmor)

        elif sattsning == "6":
            table.remove(Sexor)
            for tvåa in dice:
                if etta == 6:
                    poäng_tvåor.append(6)
            poäng_sexor = sum(poäng_sexor)

        dice = []
        choices = []
        svar = input("Vill du spela ett spel? j/n: ")

            

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




"""

        if b == 1:
            b = 0
            a = dice[1+1]
            for g in dice:
                if g == a:
                    b = b + 1
        elif b == 2:
            a = dice[2]
            for g in dice:
                if g == a:
                    c = c + 1
        elif c == 1:
            a = dice[3]
            for g in dice:
                if g == a:
                    c = c + 1
        elif b == 3:
            a = dice[3]
            for g in dice:
                if g == a:
                    c = c + 1

        if b == 2 or c == 3:
            if "7. par" in choices:
                pass
            else:
                choices.append("7. par")

        if b == 2 and c == 2:
            if "8. tvåpar" in choices:
                pass
            else:
                choices.append("8. tvåpar")
        
        elif b == 3 or c == 3:
            if "9. tretal" in choices:
                pass
            else:
                choices.append("9. tretal")

        if b == 4 or c == 4:
            if "10. fyrtal" in choices:
                pass
            else:
                choices.append("10. fyrtal")
        
        elif b == 2 and c == 3 or b == 3 and c == 2:
            if "11. kåk" in choices:
                pass
            else:
                choices.append("11. kåk")

## måst fixa så att om man har 2 par ska man kunna välja vilka som man vill lägga på par



         """      