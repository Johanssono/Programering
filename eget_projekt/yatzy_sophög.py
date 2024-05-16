dice = [1, 2, 2, 5, 5]
tvåpar = []
print(dice)



for a in dice:
    if a = dice.index(a + 1):
        dice.pop(a)
    
for a in dice:
    dice.count(a)
    d = dice.count(a)
    print(d)

    if d >= 2 and b < 4:
        tvåpar.append(a)






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

'''
                        for tal in dice:
                            if (tal == save):
                                saved.append(tal)
                                dice.remove(tal)

                        tidigare försök till att skapa en aoutomatiserad lista som tar bort och lägger in vald tärning
                        '''


        """
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
        """

        """
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
        """


        ettor = par.count(1)
        tvåor = par.count(2)
        treor = par.count(3)
        fyror = par.count(4)
        femmor = par.count(5)
        sexor = par.count(6)
        
        if len(par) >= 2:
            for alternativ in table:
                if alternativ == "Par":
                    if "7. Par" not in choices:
                        choices.append("7. Par")

       

        # är tvåpar?
        # sortera dices
        # räkna dices[0] om > 3 går ej
        # hoppa till nästa som inte har denna valör 2 2  3 5 5
        # räkna hur många om minst 2 klar
        # annars hoppa till nästa och räkna
        

        #2 2 2 5 5
        #2 2 5 5







            while par.count(a) > 1:     #Jag ska skriva en kod som använder sig av variabler för att kolla om man kan välja par, tvåpar osv.
                b = a + 1
                par.count(b)
                if a == b:
                    

                    for alternativ in table:
                        if alternativ == "Två par":
                            if "8. Två par" in choices:
                                pass



        
        elif len(par) == 4:
            if par[0] != par[0 - 1]:
                for alternativ in table:
                    if alternativ == "Par":
                        if "7. Par" not in choices:
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
                    if alternativ == "Tretal":
                        if "7. Tretal" not in choices:
                            choices.append("7. Tretal")



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