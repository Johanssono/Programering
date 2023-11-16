svar = input("Vill du spela ett spel? j/n ")

import random

mylist = ["sten", "sax", "påse"]




while svar == "j" or svar == "ja":
    if svar == "j" or svar == "ja":
        svar = input("sten! sax! påse!... ")
        game = random.choice(mylist)
        if game == "sten" and svar == "sten":
            print (game)
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif game == "sten" and svar == "sax":
            print (game)
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif game == "sten" and svar == "påse":
            print (game)
            svar = input("Du vann! grattis! Vill du spela igen?  j/n ")

        elif game == "sax" and svar == "sax":
            print (game)
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif game == "sax" and svar == "påse":
            print (game)
            svar = input("Jag vann! vill du spela igen?  j/n ")
            
        elif game == "sax" and svar == "sten":
            print (game)
            svar = input("Du vann! grattis! Vill du spela igen?  j/n ")
            
        elif game == "påse" and svar == "påse":
            print (game)
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif game == "påse" and svar == "sten":
            print (game)
            svar = input("Jag vann! vill du spela igen?  j/n ")
            
        else:
            print (game)
            svar = input("Du vann! grattis! Vill du spela igen?  j/n ")

print ("vad tråkigt, hej då")