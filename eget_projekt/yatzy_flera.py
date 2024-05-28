import random


class Player:
    def __init__(self, name):
        self.name = name
        """Poäng på vilkår 1-6 och används för att räkna ut om spelaren är behörig att få bonusen"""
        self.points = 0
        """Totala mängden poäng som spelaren har"""
        self.points_total = 0
        """En lista med alla alternativ som spelaren kan välja ifrån, används för att räkna ut valmöjligheter för spelaren"""
        self.table = {1: "Ettor", 2: "Tvåor", 3: "Treor", 4: "Fyror", 5: "Femmor", 6: "Sexor", 7: "Par", 8: "Tretal", 9: "Fyrtal", 10: "Två par", 11: "Kåk", 12: "Liten stege", 13: "Stor Stege", 14: "Yatzy", 15: "Chans"}
#Behöver göra så att man den frågar om frågan om man skriver en bokstav när den ber om en siffra


def count_of_options(potential):
    """Lägger till alt ernativ i listan choices där spelaren sedan väljer vilkår att lägga poängen på."""
    for option in participant.table:
        if option == potential:
            if participant.table[potential] not in parikng_lot:
                parikng_lot.append(participant.table[potential])
    return potential


def appropriation_of_options(parikng_lot):
    for amount in range(len(parikng_lot)):
        choices[amount + 1] = parikng_lot[amount]


def dice_counter(die):
    """Räknar ut antalet av varge tärning i listan"""
    Quantity = dice.count(die)
    return Quantity

    #Måste ändra om och returna ett svar och spara det svaret i en lista.

def bonus_counter():
    """Räknar ut om spelaren har mött kriterierna för att motag bonusen"""
    if participant.points >= 63:
        participant.points_total = participant.points_total + 50

def yatzy_counter():
    """Används för att räkna ut apelarens poäng vid val av vilkår 14"""
    participant.points_total = participant.points_total + 50

def smal_point_counter(investment, participant):
    #borde ientiligen inte använda "global", måste komma på ett annat sätt att ge funktionerna tillgång till listorna som dem arbetar med.
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 1-6 och lägger till dem i listan med poäng"""
    for die in dice:
        if die == investment:
            participant.points = participant.points + die
            participant.points_total = participant.points_total + die
            #points_total räknas som en integer och kan inte använda sig av kommandot append.
    if investment == 14:
        yatzy_counter()

def number_counter(selection):
    """Funktionen räknar antalet av varge siffra i listan med par och används för att räkna ut spelarens poäng beroende på val innom vilkåren 7-9"""
    for digit in pair:
        if pair.count(digit) >= selection and digit not in second_choice:
            if selection == 2:
                second_choice.append(digit)
            else:
                return digit
    if selection == 2:
        return second_choice

def pair_counter(investment, participant, second_choice):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 7 och lägger till dem i listan med poäng"""
    number_counter(2)
    if len(second_choice) > 1:
        checker = True
        while checker == True:
            print(second_choice)
            investment_2 = input("Skriv siffran som du vill ha par på: ")
            if investment_2.isnumeric():
                investment_2 = int(investment_2)
                if investment_2 in second_choice and isinstance(investment, int):
                    checker = False
        participant.points_total = participant.points_total + investment_2 * 2
    else:
        participant.points_total = participant.points_total + second_choice[0] * 2            


def average_point_counter(investment, participant):
    """Funktionen räknar ut pängenen om spelaren valt att lägga poängen på vilkår 8 eller 9 och legger till det i listan med poäng"""
    number = investment - 5
    participant.points_total = participant.points_total + number_counter(tal) * number

def big_point_counter(investment, participant):
    """Funktionen räknar ut poängen om spelaren har valt att lägga poängen på vilkår 10-15 och lägger till dem i listan med poäng """
    if investment == 10:
        participant.points_total = participant.points_total + pair[0] * 2 + pair[-1] * 2
        
    elif investment > 10 and investment < 12 or investment == 15:
        participant.points_total = participant.points_total + sum(pair)
    
    
    
    

def counter_chooser(investment):
    """Funktionen används för att räkna ut vilken räknefunktion som ska användas beroende på vilket vilkår spelaren valde 
    och tar bort detta alternativet så det inte kan väljas igen"""
    participant.table.pop(investment)
    if investment <=6:
        smal_point_counter(investment, participant)
    elif investment == 7:
        pair_counter(investment, participant, second_choice)
    elif investment == 8 or investment == 9:
        average_point_counter(investment, participant)
    elif investment > 9:
        big_point_counter(investment, participant)

def punishment():
    """Funktionen straffar spelaren om spelaren inte har tärningar som passar med något kvarstående alternativ, 
    detta genom att tvinga spelaren stryka ett alternativ ur listan med kvarvarande alternativ"""
    checker = True
    while checker == True:
        print(participant.table)
        sacrifice = input("Skriv siffran på den du vill stryka: ")
        if sacrifice.isnumeric():
            sacrifice = int(sacrifice)
            if isinstance(sacrifice, int) and sacrifice <= len(participant.table):
                participant.table.pop(sacrifice)
                checker = False


###skriv en deffinition som kollar om den valda sattnsningen fungerar, om det inte gör det be dem välja sattsning igen.



"""

def type_checker_srt(variabel_tempo_str):
if isinstance(variabel_tempo_str, str) and variabel_tempo_str == "j" or variabel_tempo_str == "n":

def type_checker_int(variabel_tempo_int, variabel_amount_tempo):
if isinstance(variabel_tempo_int, int) and variabel_tempo_int < variabel_amount_tempo 

"""

"En lista på spelare"
dice = []
"""En lista på antalet tärningar spelaren kan kasta efter att ha sparat tärningar"""
number_of_dice = []
Quantity = 0
throws = 3
"""En lista på sparade tärningar mellan kast"""
saved = []
"""EN lista med alternativen som spelaren har att välja mellan"""
choices = {}
parikng_lot = []
second_choice = []
pair = []

"""En nedräkning för att avgöra om spelaren är behörig till en bonus"""
bonus_countdown = 6

player = []

checker = True

while checker == True:
    antal_spelare = input("Skriv in antalet spelare: ")
    if antal_spelare.isnumeric():
        antal_spelare = int(antal_spelare)
        if isinstance(antal_spelare, int):
            checker = False

while antal_spelare > 0:
    player_name = input("skriv namn på alla spelare. En spelare i taget tack, spelar-1 kommer slumpmässigt väljas ut: ")
    player_name = Player(player_name)
    player.append(player_name)
    antal_spelare = antal_spelare - 1
    random.shuffle(player)


game_time = True

while game_time == True:
    for participant in player:
        print("Spelare: ", participant.name)
        print("Poäng: ", participant.points_total)
        print("Tabell: ", participant.table)
        throws = 3
        Quantity = 0

    #skapa while loopar så man kan srkiva fel utan att spelet avbryts

    #göra så att när spelet går in i andra omgången så ska man inte få frågan om man vill spela ett spel, utan bara om man vill kasta tärningarna

    #fixa så man kan spela fler än 1 person


        if len(participant.table) == 0:
            print("Du har tyvär inte några alternativ kvar att lägga poäng på, du får därför vänta tills alla spelat klart")
        elif len(participant.table) > 0:



            while throws > 0:

                throw = "k"
                while throw !="j" and throw !="n":
                    throw = input("Vill du kasta tärningarna? j/n: ")
                
                while throw == "j":
                    while Quantity < 5:
                        die = random.randrange(1, 7)
                        dice.append(die)
                        Quantity = Quantity + 1

                    if throws > 1:
                    
                        print(dice)

                        save_dice = "k"
                        while save_dice !="j" and save_dice !="n":
                            save_dice = input("Vill du spara några tärningar? j/n: ")

                        while save_dice == "j":

                            checker = True
                            while checker == True:
                                print(dice)
                                save = input("vilka vill du spara? 1, 2, 3, 4, 5 eller 6: ")
                                if save.isnumeric():
                                    save = int(save)
                                    if isinstance(save, int) and save < 7 and save > 0:
                                        while checker == True:
                                            amount = input("Hur många av den valda siffran vill du spara? 1, 2, 3, 4 eller 5: ")
                                            if amount.isnumeric():
                                                amount = int(amount)
                                                if isinstance(amount, int) and amount < 6 and amount > 0:
                                                    checker = False

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
                                checker = True
                                while checker == True:
                                    save_dice = input("Vill du spara några fler tärningar? j/n: ")
                                    if isinstance(save_dice, str) and save_dice == "j" or save_dice == "n":
                                        checker = False

                        print("sparade tärningar: ", saved)
                        
                        if len(saved) > 0:
                            checker = True
                            while checker == True:
                                remove_dice = input("Vill du ta bort några tärningar? j/n: ")
                                if isinstance(remove_dice, str) and remove_dice == "j" or remove_dice == "n":
                                    checker = False

                            while remove_dice == "j":
                                delete = input("1, 2, 3, 4, 5 eller 6? ")
                                if delete.isnumeric():
                                    delete = int(delete)
                                    if isinstance(delete, int) and delete < 7 and delete > 0:                        
                                        amount = input("Hur många av den valda siffran vill du spara? 1, 2, 3, 4 eller 5: ")
                                        if amount.isnumeric():
                                            amount = int(amount)
                                            if isinstance(amount, int) and amount < 6 and amount > 0:
                                                for i in range(len(dice) -1, -1, -1):
                                                    if dice[i] == delete and amount > 0:
                                                        saved.remove(save)
                                                        dice.append(save)
                                                        amount = amount - 1
                                            
                                        print("sparade tärningar: ", saved)
                            
                                checker = True
                                while checker == True:
                                    remove_dice = input("Vill du ta bort några fler tärningar? j/n: ")
                                    if isinstance(remove_dice, str) and remove_dice == "j" or remove_dice == "n":
                                        checker = False
                        dice = []

                        dice.extend(saved)

                        print(dice)
                        Quantity = len(dice)
                        throws = throws - 1

                        saved = []
                        
                        checker = True
                        while checker == True:
                            throw = input("Vill du kasta tärningarna? j/n: ")
                            if isinstance(throw, str) and throw == "j" or throw == "n":
                                checker = False
                    
                    else:
                        throws = throws - 1
                        dice.sort()
                        print(dice)
                        print(participant.table)
                        print()
                        throw = "n"
                        

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
                for die in dice:
                    if die == potential_choice:
                        #tillägning_av_alternativ Python PEP: https://peps.python.org/pep-0008/
                        count_of_options(potential_choice)
                potential_choice = potential_choice + 1


        #Jag föränklade koden nedan för att minska mängden kod att underhålla, detta gjorde jag genom en while loop som ökar värden för 
        # varge tal i listan med tärningar. Då den bara kollar från ett till sex, går det att använda mig av index för att kolla omalternativen finns,
        #detta på grund av att i listan med alternativ kommer 




            timer = 1
            count = 2

            while timer < 4:
                for die in dice:
                    if dice.count(die) >= count:
                        potential = 6 + timer
                        count_of_options(potential)
                    elif dice.count(die) == 5:
                        count_of_options(15)
                count = count + 1
                timer = timer + 1

            timer = 1
            while timer < 7:
                number_of_dice.append(dice_counter(timer))
                timer = timer + 1

            if number_of_dice[0] == 1 and number_of_dice[1] == 1 and number_of_dice[2] == 1 and number_of_dice[3] == 1 and number_of_dice[4] == 1:
                count_of_options(12)


            elif  number_of_dice[1] == 1 and number_of_dice[2] == 1 and number_of_dice[3] == 1 and number_of_dice[4] == 1 and number_of_dice[5] == 1:
                count_of_options(13)


            potential = 1

            while potential < 7:
                räkning = dice.count(potential)
                if räkning > 1:
                    for die in dice:
                        if die == potential:
                            pair.append(potential)
                potential = potential + 1


            if len(pair) >= 4:
                if pair[0] != pair[0 - 1] and len(pair) == 4:
                    count_of_options(10)

                if pair[0] != pair[0 - 1] and len(pair) == 5:
                    count_of_options(10)
                    count_of_options(11)



            for option in participant.table:
                if option == 15:
                    if participant.table[15] not in choices:
                        parikng_lot.append(participant.table[15])            
            
            appropriation_of_options(parikng_lot)

            if len(choices) == 0:
                punishment()
            else:
                checker = True
                while checker == True:
                    print(choices)
                    investment = input("Skriv siffran på alternativet du önskar välja: ")
                    if investment.isnumeric():
                        investment = int(investment)
                        if isinstance(investment, int) and investment <= len(choices):
                            checker = False
                
                counter_chooser(investment)

                if investment > 0 and investment < 6:
                    bonus_countdown = bonus_countdown - 1
                    if bonus_countdown == 0:
                        bonus_counter()

            if participant.points > 0:

                print("Dina samanlagda poäng i vilkår 1-6: ", participant.points)
            
            print("Dina sammanlagda poäng i alla vilkår: ", participant.points_total)

            dice = []
            choices = {}
            pair = []
            if len(player[-1].table) == 0:
                game_time = False   

highest_points = player[0].points_total
winner = player[0].name

for participant in player:
    if participant.points_total > highest_points:
        highest_points = participant.points_total
        winner = player[participant.name]
    print(participant.points_total)

print("vinnaren är: ", winner, "med", highest_points, "poäng")
