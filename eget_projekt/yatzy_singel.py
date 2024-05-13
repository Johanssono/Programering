import random



def TillägningAvAlternativ(potential):
    """Lägger till alternativ i listan choices där spelaren sedan väljer vilkår att lägga poängen på."""
    for alternativ in table:
        if alternativ == potential:
            if table[potential] not in choices:
                choices.append(table[potential])
    return potential

def DiceCounter(tärning):
    """Räknar ut antalet av varge tärning i listan"""
    antal = dice.count(tärning)
    return antal

    #Måste ändra om och returna ett svar och spara det svaret i en lista.

def BonusCounter():
    """Räknar ut om spelaren har mött kriterierna för att motag bonusen"""
    if sum(points) >= 63:
        points_total.append(50)

def YatzyCounter():
    """Används för att räkna ut apelarens poäng vid val av vilkår 14"""    
    points_total.append(50)

def SmalPointCounter(sattsning, points, points_total):
    #borde ientiligen inte använda "global", måste komma på ett annat sätt att ge funktionerna tillgång till listorna som dem arbetar med.
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 1-6 och lägger till dem i listan med poäng"""
    for tärning in dice:
        if tärning == sattsning:
            points.append(tärning)
            points_total.append(tärning)
            #points_total räknas som en integer och kan inte använda sig av kommandot append.
    if sattsning == 14:
        YatzyCounter()

def NumberCounter(val):
    """Funktionen räknar antalet av varge siffra i listan med par och används för att räkna ut spelarens poäng beroende på val innom vilkåren 7-9"""
    for siffra in par:
        if par.count(siffra) >= val and siffra not in second_choice:
            second_choice.append(siffra)   
            return siffra


def ParCounter(sattsning, points_total):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 7 och lägger till dem i listan med poäng"""
    NumberCounter(2)
    if len(second_choice) > 1:
        while sattsning_2 not in second_choice:
            sattsning_2 = input("Skriv siffran som du vill ha par på")
        points_total.append(sattsning_2 * 2)
    else:
        points_total.append(second_choice[0])
            


def AvragePointCounter(sattsning, points_total):
    """Funktionen räknar ut pängenen om spelaren valt att lägga poängen på vilkår 8 eller 9 och legger till det i listan med poäng"""
    tal = sattsning - 5
    points_total.append(NumberCounter(tal) * tal)


def BigPointCounter(sattsning, points_total):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 10-15 och lägger till dem i listan med poäng """
    if sattsning == 10:
        points_total.append(par[0] * 2 + par[-1] * 2)
    elif sattsning > 10 and sattsning != 15:
        points_total.append(sum(par))
    elif sattsning == 15:
        points_total.append(sum(dice))

def ChoiseOfPointCounter(sattsning):
    """Funktionen används för att räkna ut vilken räknefunktion som ska användas beroende på vilket vilkår spelaren valde 
    och tar bort detta alternativet så det inte kan väljas igen"""
    table.pop(sattsning)
    if sattsning <=6:
        SmalPointCounter(sattsning, points, points_total)
    elif sattsning == 7:
        ParCounter(sattsning, points_total)
    elif sattsning  == 8 or sattsning == 9:
        AvragePointCounter(sattsning, points_total)
    elif sattsning > 9:
        BigPointCounter(sattsning, points_total)

def Punishment():
    """Funktionen straffar spelaren om spelaren inte har tärningar som passar med något kvarstående alternativ, 
    detta genom att tvinga spelaren stryka ett alternativ ur listan med kvarvarande alternativ"""
    print(table)
    sacrifice = input("Skriv siffran på den du vill stryka")
    table.pop(sacrifice)

"""Lista med poäng på vilkår 1-6 och används för att räkna ut om spelaren är behörig att få bonusen"""
points = []
"""En lista med den totala mängden poäng"""
points_total = []
"En lista på spelare"
player = []
dice = []
"""En lista på antalet tärningar spelaren kan kasta efter att ha sparat tärningar"""
antal_tärningar = []
antal = 5
"""En lista på sparade tärningar mellan kast"""
saved = []
"""En lista med alla alternativ som spelaren kan välja ifrån, används för att räkna ut valmöjligheter för spelaren"""
table = {1: "1. Ettor", 2: "2. Tvåor", 3: "3. Treor", 4: "4. Fyror", 5: "5. Femmor", 6: "6. Sexor", 7: "7. Par", 8: "8. Tretal", 9: "9. Fyrtal", 10: "10. Två par", 11: "11. Kåk", 12:"12. Liten stege", 13:"13. Stor Stege", 14: "14. Yatzy", 15: "15. Chans"}
"""En lista som innehåller alla alternativ och används för att ta bort och strycka alternativ och visar spelaren vilka kvarstående alternativ som finns kvar"""
offer_table = {1: "1. Ettor", 2: "2. Tvåor", 3: "3. Treor", 4: "4. Fyror", 5: "5. Femmor", 6: "6. Sexor", 7: "7. Par", 8: "8. Tretal", 9: "9. Fyrtal", 10: "10. Två par", 11: "11. Kåk", 12:"12. Liten stege", 13:"13. Stor Stege", 14: "14. Yatzy", 15: "15. Chans"}
"""EN lista med alternativen som spelaren har att välja mellan"""
choices = []
second_choice = []
par = []

"""En nedräkning för att avgöra om spelaren är behörig till en bonus"""
bonus_countdown = 6

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
                        if len(saved) > 0:
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
        print(dice)
        potential_choice = dice[0]

        while potential_choice < 7:
            for tärning in dice:
                if tärning == potential_choice:
                    TillägningAvAlternativ(potential_choice)
            potential_choice = potential_choice + 1


#Jag föränklade koden nedan för att minska mängden kod att underhålla, detta gjorde jag genom en while loop som ökar värden för 
# varge tal i listan med tärningar. Då den bara kollar från ett till sex, går det att använda mig av index för att kolla omalternativen finns,
#detta på grund av att i listan med alternativ kommer 




        timer = 1
        count = 2

        while timer < 3:
            for tärning in dice:
                if dice.count(tärning) == count:
                    potential = 6 + timer
                    TillägningAvAlternativ(potential)
                elif dice.count(tärning) == 5:
                    TillägningAvAlternativ(15)
            count = count + 1
            timer = timer + 1

        timer = 1
        while timer < 7:
            antal_tärningar.append(DiceCounter(timer))
            timer = timer + 1

        if antal_tärningar[0] == 1 and antal_tärningar[1] == 1 and antal_tärningar[2] == 1 and antal_tärningar[3] == 1 and antal_tärningar[4] == 1:
            TillägningAvAlternativ(12)


        elif  antal_tärningar[1] == 1 and antal_tärningar[2] == 1 and antal_tärningar[3] == 1 and antal_tärningar[4] == 1 and antal_tärningar[5] == 1:
            TillägningAvAlternativ(13)


        potential = 1

        while potential < 7:
            räkning = dice.count(potential)
            if räkning > 1:
                for tärning in dice:
                    if tärning == potential:
                        par.append(potential)
            potential = potential + 1


        if len(par) >= 4:
            if par[0] != par[0 - 1] and len(par) == 4:
                TillägningAvAlternativ(10)

            if par[0] != par[0 - 1] and len(par) == 5:
                TillägningAvAlternativ(10)
                TillägningAvAlternativ(11)



        for alternativ in table:
            if alternativ == 15:
                if table[15] not in choices:
                   choices.append(table[15])            
        

        print(choices)

        if len(choices) == 0:
            Punishment()
        else:
            sattsning = int(input("Skriv siffran på alternativet du önskar välja: "))
            ChoiseOfPointCounter(sattsning)

            if sattsning > 0 and sattsning < 6:
                bonus_countdown = bonus_countdown - 1
                if bonus_countdown == 0:
                    BonusCounter()

        #behöver komma på ett sätt att räkna vad dem kan välja att ta par på om det finns mer än 1 par och liknande.

        if sum(points) > 0:

            print("Dina samanlagda poäng i vilkår 1-6: ", sum(points))
        
        print("Dina sammanlagda poäng i alla vilkår: ", sum(points_total))



        

        dice = []
        choices = []
        par = []
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