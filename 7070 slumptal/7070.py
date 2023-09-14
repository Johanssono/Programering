svar = input("Vill du spela ettt spel? j/n ")

import random
if svar == "j":
    a = random.randrange(7)
    print(a)
    b = random.randrange(7)
    print(b)
    if b != a:
        print("Du förlorade, vill du spela igen? j/n ")
    else:
        print ("DU vann, grattis!!")