

svar = input("Vill du spela ettt spel? j/n ")

import random
while svar == "j":
    if svar == "j":
        a = random.randrange(7)
        print(a)
        b = random.randrange(7)
        print(b)

        if b != a:
            svar = input("Du förlorade, vill du spela igen? j/n ")
               
        else:
            print ("DU vann, grattis!!")
            svar = "n"