svar = input("Vill du spela ett spel? j/n ")

import random





while svar == "j" or svar == "ja":
    if svar == "j" or svar == "ja":
        svar = input("sten! sax! påse!... ")
        
        a = random.randrange(1,4)
        if a == 1 and svar == "sten":
            print ("sten")
            svar =input("Det blev lika, vill du spela igen?  j/n ")
            
        elif a == 1 and svar == "sax":
            print ("sten")
            svar = input("Jag vann! Vill du spela igen?  j/n ")
            
        elif a == 1 and svar == "påse":
            print ("sten")
            svar = input("Du vann! grattis! Vill du spela igen?  j/n ")
            
        
        elif a == 2 and svar == "sax":
            print ("sax")
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif a == 2 and svar == "påse":
            print ("sax")
            svar = input("Jag vann! Vill du spela igen?  j/n ")
            
        elif a == 2 and svar == "sten":
            print ("sax")
            svar = input("Du vann! grattis! Vill du spela igen?  j/n ")
            
        elif a == 3 and svar == "påse":
            print ("påse")
            svar = input("Det blev lika, vill du spela igen?  j/n ")
            
        elif a == 3 and svar == "sten":
            print ("påse")
            svar= input("Jag vann! Vill du spela igen?  j/n ")
            
        else:
            print ("påse")
            svar =input("Du vann! grattis! Vill du spela igen?  j/n ")
            
print ("vad tråkigt, hej då")