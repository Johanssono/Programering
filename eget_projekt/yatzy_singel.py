import random

def TillägningAvAlternativ():
    for alternativ in table:
                if alternativ == potential:
                    if table[potential] not in choices:
                        choices.append(table[potential])

def DiceCounter():
    ettor = dice.count(1)
    tvåor = dice.count(2)
    treor = dice.count(3)
    fyror = dice.count(4)
    femmor = dice.count(5)
    sexor = dice.count(6)

    #Måste ändra om och returna ett svar och spara det svaret i en lista.

def PointCounterSmall():
    if sattsning >= 6:
        offer_table.remove(sattsning)
        for tärning in dice:
            if tärning == sattsning:
                poäng.append(tärning)
        poäng = sum(poäng)
    elif sattsning == 14:
        offer_table.remove(sattsning)
        poäng.append(tärning)
        poäng = sum(poäng)




player = []
dice = []
antal = 5
saved = []
table = {1: "Ettor", 2: "Tvåor", 3: "Treor", 4: "Fyror", 5: "Femmor", 6: "Sexor", 7: "Par", 8: "Tretal", 9: "Fyrtal", 10: "Två par", 11: "Kåk", 12:"Liten stege", 13:"Stor Stege", 14: "Yatzy", 15: "Chans"}
offer_table = ["1. Ettor", "2. Tvåor", "3. Treor", "4. Fyror", "5. Femmor", "6. Sexor", "7. Par", "8. Tretal", "9. Fyrtal", "10. Två par", "11. Kåk", "12. Liten stege", "13. Stor Stege", "14. Yatzy", "15. Chans"]
choices = []
par = []


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

                                
                                # Denna for slinga kollar igenom listan "dice" och lägger in dem i 
                                # listan "saved", men for slingan kollar igenom listan "dice" backlänges 
                                # för att int ändra index-värdet hos objekten i listan och garantera att 
                                # alla bjekt av samma värde tas bort oavsätt index
                                


                        
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

        dice = [5, 5, 5, 5, 5]
        print(dice)
        potential = dice[0]

        while potential < 7:
            for tärning in dice:
                if tärning == potential:
                    TillägningAvAlternativ()
            potential = potential + 1


#Jag föränklade koden nedan för att minska mängden kod att underhålla, detta gjorde jag genom en while loop som ökar värden för 
# varge tal i listan med tärningar. Då den bara kollar från ett till sex, går det att använda mig av index för att kolla omalternativen finns,
#detta på grund av att i listan med alternativ kommer 




        timer = 1
        count = 2

        while timer < 3:
            for tärning in dice:
                if dice.count(tärning) == count:
                    potential = 6 + timer
                    TillägningAvAlternativ()
                elif dice.count(tärning) == 5:
                    potential = 15
                    TillägningAvAlternativ()
            count = count + 1
            timer = timer + 1

        DiceCounter()

        if ettor == 1 and tvåor == 1 and treor == 1 and fyror == 1 and femmor == 1:
            potential = 12
            TillägningAvAlternativ()


        elif  tvåor == 1 and treor == 1 and fyror == 1 and femmor == 1 and sexor == 1:
            potential = 13
            TillägningAvAlternativ()


        potential = 1

        while variabel < 7:
            räkning = dice.count(potential)
            if räkning > 1:
                for tärning in range:
                    if dice[tärning] == potential:
                        par.append(potential)
            potential = potential + 1


        if len(par) >= 4:
            if par[0] != par[0 - 1] and len(par) == 4:
                potential = 10
                TillägningAvAlternativ()

            elif par[0] != par[0 - 1] and len(par) == 5:
                potential = 11
                TillägningAvAlternativ


        for alternativ in table:
            if alternativ == 15:
                if "Chans" not in choices:
                   choices.append("Chans")            
        

        print(choices)

        sattsning = input("Skriv siffran på alternativet du önskar välja: ")


        PointCounterSmall()




       

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