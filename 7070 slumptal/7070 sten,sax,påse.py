svar = input("Vill du spela sten, sax, påse? j/n ")

import random

mylist = ["sten", "sax", "påse"]






if svar == "j":
    game = print(random.choice(mylist))
    if game == "sten" and svar == "sten":
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "sten" and svar == "sax":
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "sten" and svar == "påse":
        input("Du van, grattis! Vill du spela igen?  j/n ")
        
    
    elif game == "sax" and svar == "sax":
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "sax" and svar == "påse":
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "sax" and svar == "sten":
        input("Du van, grattis! Vill du spela igen?  j/n ")
        

    elif game == "påse" and svar == "påse":
        input("Det blev lika, vill du spela igen?  j/n ")
        
    elif game == "påse" and svar == "sten":
        input("Jag van! Vill du spela igen?  j/n ")
        
    elif game == "påse" and svar == "sax":
        input("Du van, grattis! Vill du spela igen?  j/n ")
        
else:
    print ("DU vann, grattis!!")
    