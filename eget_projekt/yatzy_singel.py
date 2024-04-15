import random

player = []
dice = []
antal = 5
saved = []
table = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor", "Par", "Två par", "Tretal", "Fyrtal", "Kåk", "Liten stege", "Stor Stege","Yatzy", "Chans"]
choices = []
par = []
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

        dice = [3, 3, 5, 5, 6]
        print(dice)

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
                        if "2. Tvåor" in choices:
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
        if tvåor > 1:
            for i in range(len(dice) -1, -1, -1):
                if dice[i] == 2:
                    par.append(2)
                    dice.remove(2)
        if treor > 1:
            for i in range(len(dice) -1, -1, -1):
                if dice[i] == 3:
                    par.append(3)
                    dice.remove(3)
        if fyror > 1:
            for i in range(len(dice) -1, -1, -1):
                if dice[i] == 4:
                    par.append(4)
                    dice.remove(4)
        if femmor > 1:
            for i in range(len(dice) -1, -1, -1):
                if dice[i] == 5:
                    par.append(5)
                    dice.remove(5)
        if sexor > 1:
            for i in range(len(dice) -1, -1, -1):
                if dice[i] == 6:
                    par.append(6)
                    dice.remove(6)

        
        

        ettor = par.count(1)
        tvåor = par.count(2)
        treor = par.count(3)
        fyror = par.count(4)
        femmor = par.count(5)
        sexor = par.count(6)
        
        if len(par) == 2:
            for alternativ in table:
                if alternativ == "Par":
                    if "7. Par" in choices:
                        pass
                    else:
                        choices.append("7. Par")

        elif len(par) == 4:
            if par[0] != par[0 - 1]:
                for alternativ in table:
                    if alternativ == "Par":
                        if "7. Par" in choices:
                            pass
                        else:
                            choices.append("7. Par")
            if ettor == 2 or tvåor == 2 or treor == 2 or fyror == 2 or femmor == 2 or sexor == 2:
                for alternativ in table:
                    if alternativ == "Två par":
                        if "8. Två par" in choices:
                            pass
                        else:
                            choices.append("8. Två par")
            elif ettor == 4 or tvåor == 4 or treor == 4 or fyror == 4 or femmor == 4 or sexor == 4:
                for alternativ in table:
                        if alternativ == "Fyrtal":
                            if "10. Fyrtal" in choices:
                                pass
                            else:
                                choices.inset("10. Fyrtal")


        elif len(par) == 3:
            for alternativ in table:
                if alternativ == "Tretal":
                    if "9. Tretal" in choices:
                        pass
                    elif "10. Fyrtal" in choices:
                            choices.insert(9, "9. Tretal")
                    else:
                        choices.append("9. Tretal")



        elif len(par) == 5:
            ettor = dice.count(1)
            tvåor = dice.count(2)
            treor = dice.count(3)
            fyror = dice.count(4)
            femmor = dice.count(5)
            sexor = dice.count(6)
            if ettor > 1 and ettor < 4 or tvåor > 1 and tvåor < 4 or treor > 1 and treor < 4 or fyror > 1 and fyror < 4 or femmor > 1 and femmor < 4 or sexor > 1 and sexor < 4:
                for alternativ in table:
                    if alternativ == "Kåk":
                        if "11. Kåk" in choices:
                            pass
                        else:
                            choices.append("11. Kåk")
            elif ettor == 5 or tvåor == 5 or treor == 5 or fyror == 5 or femmor == 5 or sexor == 5:
                for alternativ in table:
                    if alternativ == "Yatzy":
                        if "15. Yatzy" in choices:
                            pass
                        else:
                            choices.append("15. Yatzy")

        for alternativ in table:
                    if alternativ == "Chans":
                        if "16. Chans" in choices:
                            pass
                        else:
                            choices.append("16. Chans")

                    
        

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
            if "8. Två par" in choices:
                pass
            else:
                choices.append("8. Två par")
        
        elif b == 3 or c == 3:
            if "9. Tretal" in choices:
                pass
            else:
                choices.append("9. Tretal")

        if b == 4 or c == 4:
            if "10. fyrtal" in choices:
                pass
            else:
                choices.append("10. fyrtal")
        
        elif b == 2 and c == 3 or b == 3 and c == 2:
            if "11. Kåk" in choices:
                pass
            else:
                choices.append("11. Kåk")

## måst fixa så att om man har 2 par ska man kunna välja vilka som man vill lägga på par



         """      