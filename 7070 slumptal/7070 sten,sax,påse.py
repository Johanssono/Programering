svar = input("Vill du spela ett spel? j/n ")

import random

mylist = ["sten", "sax", "påse"]





print("VÄLKOMMEN")
if svar == "j":
    svar = input("sten! sax! påse!... ")
    game = random.choice(mylist)
    if game == "sten" and svar == "sten":
        print = game
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "sten" and svar == "sax":
        print = game
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "sten" and svar == "påse":
        print = game
        input("Du van, grattis! Vill du spela igen?  j/n ")

        
    elif game == "sax" and svar == "sax":
        print = game
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "sax" and svar == "påse":
        print = game
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "sax" and svar == "sten":
        print = game
        input("Du van, grattis! Vill du spela igen?  j/n ")
        

    elif game == "påse" and svar == "påse":
        print = game
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "påse" and svar == "sten":
        print = game
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "påse" and svar == "sax":
        print = game
        input("Du van, grattis! Vill du spela igen?  j/n ")
        
    else:
        print ("DU vann, grattis!!")
    