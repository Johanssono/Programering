import random



def tillägning_av_alternativ(potential):
    """Lägger till alternativ i listan choices där spelaren sedan väljer vilkår att lägga poängen på."""
    for alternativ in table:
        if alternativ == potential:
            if table[potential] not in choices:
                choices.append(table[potential])
    return potential

def dice_counter(tärning):
    """Räknar ut antalet av varge tärning i listan"""
    antal = dice.count(tärning)
    return antal

    #Måste ändra om och returna ett svar och spara det svaret i en lista.

def bonus_counter():
    """Räknar ut om spelaren har mött kriterierna för att motag bonusen"""
    if sum(points) >= 63:
        points_total.append(50)

def yatzy_counter():
    """Används för att räkna ut apelarens poäng vid val av vilkår 14"""    
    points_total.append(50)

def smal_point_counter(sattsning, points, points_total):
    #borde ientiligen inte använda "global", måste komma på ett annat sätt att ge funktionerna tillgång till listorna som dem arbetar med.
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 1-6 och lägger till dem i listan med poäng"""
    for tärning in dice:
        if tärning == sattsning:
            points.append(tärning)
            points_total.append(tärning)
            #points_total räknas som en integer och kan inte använda sig av kommandot append.
    if sattsning == 14:
        yatzy_counter()

def number_counter(val):
    """Funktionen räknar antalet av varge siffra i listan med par och används för att räkna ut spelarens poäng beroende på val innom vilkåren 7-9"""
    for siffra in par:
        if par.count(siffra) >= val and siffra not in second_choice:
            if val == 2:
                second_choice.append(siffra)
            else:
                return siffra
    if val == 2:
        return second_choice

def par_counter(sattsning, points_total, second_choice):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 7 och lägger till dem i listan med poäng"""
    number_counter(2)
    if len(second_choice) > 1:
        midget = True
        while midget == True:
            print(second_choice)
            sattsning_2 = int(input("Skriv siffran som du vill ha par på: "))
            if sattsning_2 in second_choice:
                midget = False
        points_total.append(sattsning_2 * 2)
    else:
        points_total.append(second_choice[0] * 2)
            


def average_point_counter(sattsning, points_total):
    """Funktionen räknar ut pängenen om spelaren valt att lägga poängen på vilkår 8 eller 9 och legger till det i listan med poäng"""
    tal = sattsning - 5
    points_total.append(number_counter(tal) * tal)


def big_point_counter(sattsning, points_total):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 10-15 och lägger till dem i listan med poäng """
    if sattsning == 10:
        points_total.append(par[0] * 2 + par[-1] * 2)
    elif sattsning > 10 and sattsning != 15:
        points_total.append(sum(par))
    elif sattsning == 15:
        points_total.append(sum(dice))

def counter_chooser(sattsning):
    """Funktionen används för att räkna ut vilken räknefunktion som ska användas beroende på vilket vilkår spelaren valde 
    och tar bort detta alternativet så det inte kan väljas igen"""
    table.pop(sattsning)
    if sattsning <=6:
        smal_point_counter(sattsning, points, points_total)
    elif sattsning == 7:
        par_counter(sattsning, points_total, second_choice)
    elif sattsning  == 8 or sattsning == 9:
        average_point_counter(sattsning, points_total)
    elif sattsning > 9:
        big_point_counter(sattsning, points_total)

def punishment():
    """Funktionen straffar spelaren om spelaren inte har tärningar som passar med något kvarstående alternativ, 
    detta genom att tvinga spelaren stryka ett alternativ ur listan med kvarvarande alternativ"""
    print(table)
    sacrifice = input("Skriv siffran på den du vill stryka")
    table.pop(sacrifice)

def type_checker_srt():
    if isinstance(kasta, str) and kasta == "j" or kasta == "n":

def type_checker_int():

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
"""EN lista med alternativen som spelaren har att välja mellan"""
choices = []
second_choice = []
par = []

"""En nedräkning för att avgöra om spelaren är behörig till en bonus"""
bonus_countdown = 6

namn = input("Skriv namn på spelare: ")
player.append(namn)

svar = "k"
while svar !="j" and svar !="n":
    svar = input("Vill du spela ett spel? j/n: ")

if svar == "j":











































#skapa while loopar så man kan srkiva fel utan att spelet avbryts

#göra så att när spelet går in i andra omgången så ska man inte få frågan om man vill spela ett spel, utan bara om man vill kasta tärningarna

#fixa så man kan spela fler än 1 person








































    while svar == "j":
        antal = 0
        throw = 3

        while throw > 0:

            kasta = "k"
            while kasta !="j" and kasta !="n":
                kasta = input("Vill du kasta tärningarna? j/n: ")
            
            while kasta == "j":
                while antal < 5:
                    tärning = random.randrange(1, 7)
                    dice.append(tärning)
                    antal = antal + 1

                if throw > 1:
                
                    print(dice)

                    save_dice = "k"
                    while save_dice !="j" and save_dice !="n":
                        save_dice = input("Vill du spara några tärningar? j/n: ")

                    while save_dice == "j":

                        midget = True
                        while midget == True:
                            print(dice)
                            save = int(input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: "))
                            if isinstance(save, int) and save < 7:
                                amount = int(input("Hur många av den valda siffran vill du spara? 1, 2, 3, 4 eller 5: "))
                                if isinstance(amount, int) and amount < 6:
                                    midget = False
   
                        for i in range(len(dice) -1, -1, -1):
                            if dice[i] == save and amount > 0:
                                saved.append(save)
                                dice.remove(save)
                                amount = amount - 1

                                
                                # Denna for slinga kollar igenom listan "dice" och lägger in dem i 
                                # listan "saved", men for slingan kollar igenom listan "dice" backlänges 
                                # för att int ändra index-värdet hos objekten i listan och garantera att 
                                # alla bjekt av samma värde tas bort oavsätt index
                                                        
                        print(dice)
                        if len(saved) > 0:
                            midget = True
                            while midget == True:
                                save_dice = input("Vill du spara några fler tärningar? j/n: ")
                                if isinstance(save_dice, str) and save_dice == "j" or save_dice == "n":
                                    midget = False

                    print("sparade tärningar: ", saved)
                    
                    midget = True
                    while midget == True:
                        remove_dice = input("Vill du ta bort några tärningar? j/n: ")
                        if isinstance(remove_dice, str) and remove_dice == "j" or remove_dice == "n":
                            midget = False

                    while remove_dice == "j":
                        delete = input("1, 2, 3, 4, 5 eller 6? ")
                        
                        amount = int(input("Hur många av den valda siffran vill du spara? 1, 2, 3, 4 eller 5: "))
                        
                        for i in range(len(dice) -1, -1, -1):
                            if dice[i] == delete and amount > 0:
                                saved.remove(save)
                                dice.append(save)
                                amount = amount - 1
                        
                        print("sparade tärningar: ", saved)
                    
                        midget = True
                        while midget == True:
                            remove_dice = input("Vill du ta bort några fler tärningar? j/n: ")
                            if isinstance(remove_dice, str) and remove_dice == "j" or remove_dice == "n":
                                midget = False
                    dice = []

                    dice.extend(saved)

                    print(dice)
                    antal = len(dice)
                    throw = throw - 1

                    saved = []
                    
                    midget = True
                    while midget == True:
                        kasta = input("Vill du kasta tärningarna? j/n: ")
                        if isinstance(kasta, str) and kasta == "j" or kasta == "n":
                            midget = False
                
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
                    #tillägning_av_alternativ Python PEP: https://peps.python.org/pep-0008/
                    tillägning_av_alternativ(potential_choice)
            potential_choice = potential_choice + 1


#Jag föränklade koden nedan för att minska mängden kod att underhålla, detta gjorde jag genom en while loop som ökar värden för 
# varge tal i listan med tärningar. Då den bara kollar från ett till sex, går det att använda mig av index för att kolla omalternativen finns,
#detta på grund av att i listan med alternativ kommer 




        timer = 1
        count = 2

        while timer < 4:
            for tärning in dice:
                if dice.count(tärning) >= count:
                    potential = 6 + timer
                    tillägning_av_alternativ(potential)
                elif dice.count(tärning) == 5:
                    tillägning_av_alternativ(15)
            count = count + 1
            timer = timer + 1

        timer = 1
        while timer < 7:
            antal_tärningar.append(dice_counter(timer))
            timer = timer + 1

        if antal_tärningar[0] == 1 and antal_tärningar[1] == 1 and antal_tärningar[2] == 1 and antal_tärningar[3] == 1 and antal_tärningar[4] == 1:
            tillägning_av_alternativ(12)


        elif  antal_tärningar[1] == 1 and antal_tärningar[2] == 1 and antal_tärningar[3] == 1 and antal_tärningar[4] == 1 and antal_tärningar[5] == 1:
            tillägning_av_alternativ(13)


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
                tillägning_av_alternativ(10)

            if par[0] != par[0 - 1] and len(par) == 5:
                tillägning_av_alternativ(10)
                tillägning_av_alternativ(11)



        for alternativ in table:
            if alternativ == 15:
                if table[15] not in choices:
                   choices.append(table[15])            
        

        print(choices)

        if len(choices) == 0:
            punishment()
        else:
            midget = True
            while midget == True:
                sattsning = int(input("Skriv siffran på alternativet du önskar välja: "))
                if isinstance(sattsning, int) and sattsning > 16:
                    midget = False
            
            counter_chooser(sattsning)

            if sattsning > 0 and sattsning < 6:
                bonus_countdown = bonus_countdown - 1
                if bonus_countdown == 0:
                    bonus_counter()

        #behöver komma på ett sätt att räkna vad dem kan välja att ta par på om det finns mer än 1 par och liknande.

        if sum(points) > 0:

            print("Dina samanlagda poäng i vilkår 1-6: ", sum(points))
        
        print("Dina sammanlagda poäng i alla vilkår: ", sum(points_total))



        

        dice = []
        choices = []
        par = []
            

else:
    print("hej då")
