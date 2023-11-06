print ("Hej, vilken enhetskonverterare vill du använda?")
svar = input(" 1: C -> F, 2: C -> K, 3: F -> C, 4: F -> K, 5: K -> C, 6: K -> F?")

if svar == 1:
    def celciustofarenhite(C):   
        F = (9/5) * C + 32
        return F
        a = float(input("skriv temperatur i celcius: ")) 
        print (celciustofarenhite(a))

elif svar == 2:
    def celciustokelvin(C):
        K = C + 237.15
        return K
        a = float(input("Skriv temperatur i celcius: "))
        print(celciustokelvin(a))

elif svar == 3:
    def farenhitetocelcius(F):
        C = (5/9) * F -32
        return C
        a = float(input("Skriv temperatur i farenhite: "))
        print (farenhitetocelcius(a))

elif svar == 4:
    def farenhitetokelvin(F):   
        K = ((5/9) * F -32) + 237.15
        return F
        a = float(input("skriv temperatur i celcius: ")) 
        print (farenhitetokelvin(a))

elif svar == 5:
    def kelvintocelcius(K):
        C = K - 237.15
        return K
        a = float(input("Skriv temperatur i celcius: "))
        print(kelvintocelcius(a))

else svar == 6: 
    def kelvintofarenhite(K):
        F = ((9/5) * C + 32) - 237.15
        return C
        a = float(input("Skriv temperatur i farenhite: "))
        print (kelvintofarenhite(a))