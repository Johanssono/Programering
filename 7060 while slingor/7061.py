svar = input("Gisssa ett nummer! ")

while svar != 7:
    svar= input("Försök igen!")
    svar = int(svar)
    if svar < 10:
        svar = input ("Kankse lite lågt, gissa igen! ")
    elif svar > 83:
        svar = input ("Något för högt kanske, försök en igen! ")
    elif svar == 68:
        svar = input("Nära, men inte rätt, en gång till! ")
    elif svar == 69:
        svar = input("Aahhhh, du trodde! ")
    elif svar == 70:
        svar = inputs("Nära, men inte rätt, igen! ")
print("grattis, du lyckades slösa bort ditt liv med en värdelös lek")