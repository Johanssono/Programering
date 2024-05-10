import random



def TillägningAvAlternativ(potential):
    for alternativ in table:
        if alternativ == potential:
            if table[potential] not in choices:
                choices.append(table[potential])
    return potential

def DiceCounter(tärning):
    antal = dice.count(tärning)
    return antal

    #Måste ändra om och returna ett svar och spara det svaret i en lista.

def BonusCounter():
    if sum(points) >= 63:
        points_total.append(50)
    points_total = sum(points_total)

def YatzyCounter():
        points_total.append(50)
        points_total = sum(points_total)

def SmalPointCounter(sattsning):
    global bonus_countdown
    global points
    global points_total

    #borde ientiligen inte använda "global", måste komma på ett annat sätt att ge funktionerna tillgång till listorna som dem arbetar med.

    for tärning in dice:
        if tärning == sattsning:
            points.append(tärning)
            points_total.append(tärning)
            #points_total räknas som en integer och kan inte använda sig av kommandot append.
    points = sum(points)
    points_total = sum(points_total)
    bonus_countdown = bonus_countdown - 1
    if bonus_countdown == 0:
        BonusCounter()
    if sattsning == 14:
        YatzyCounter()

def NumberCounter(val):
    for siffra in par:
        if par.count(siffra) >= val and siffra not in second_choice:
            second_choice.append(siffra)   
            return siffra


def ParCounter(sattsning):
    global points_total
    NumberCounter(2)
    if len(second_choice) > 1:
        while sattsning_2 not in second_choice:
            sattsning_2 = input("Skriv siffran som du vill ha par på")
        points_total.append(sattsning_2 * 2)
    else:
        points_total.append(second_choice[0])
            
    points_total = sum(points_total)


def AvragePointCounter(sattsning):
    global points_total
    tal = sattsning - 5
    points_total.append(NumberCounter(tal) * tal)
    points_total = sum(points_total)


def BigPointCounter(sattsning):
    global points_total

    if sattsning == 10:
        points_total.append(par[0] * 2 + par[-1] * 2)
        points_total = sum(points_total)

    if sattsning > 10:
        points_total.append(sum(par))
        points_total = sum(points_total)

def ChoiseOfPointCounter(sattsning):
    table.pop(sattsning)
    if sattsning <=6:
        SmalPointCounter(sattsning)
    elif sattsning == 7:
        ParCounter(sattsning)
    elif sattsning  == 8 or sattsning == 9:
        AvragePointCounter(sattsning)
    elif sattsning > 9:
        BigPointCounter(sattsning)

def Punishment():
    print(table)
    sacrifice = print("Skriv siffran på den du vill stryka")
    table.pop(sacrifice)


points = []
points_total = []
player = []
dice = []
antal_tärningar = []
antal = 5
saved = []
table = {1: "1. Ettor", 2: "2. Tvåor", 3: "3. Treor", 4: "4. Fyror", 5: "5. Femmor", 6: "6. Sexor", 7: "7. Par", 8: "8. Tretal", 9: "9. Fyrtal", 10: "10. Två par", 11: "11. Kåk", 12:"12. Liten stege", 13:"13. Stor Stege", 14: "14. Yatzy", 15: "15. Chans"}
offer_table = {1: "1. Ettor", 2: "2. Tvåor", 3: "3. Treor", 4: "4. Fyror", 5: "5. Femmor", 6: "6. Sexor", 7: "7. Par", 8: "8. Tretal", 9: "9. Fyrtal", 10: "10. Två par", 11: "11. Kåk", 12:"12. Liten stege", 13:"13. Stor Stege", 14: "14. Yatzy", 15: "15. Chans"}
choices = []
second_choice = []
par = []

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
        dice = [2]
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

        #behöver komma på ett sätt att räkna vad dem kan välja att ta par på om det finns mer än 1 par och liknande.

        if points[0] > 0:

        #Av någon anledning kan man inte räkna en lista som ett integer, måste fixa det ellet komma på ett annat sätt att avgöra om man ska säga vad dem har för poäng på vilkår 1-6
            print("Dina samanlagda poäng i vilkår 1-6: ", points)
        
        print("Dina sammanlagda poäng i alla vilkår: ", points_total)



        

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