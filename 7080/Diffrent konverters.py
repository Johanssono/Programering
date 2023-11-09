print ("Hej, vilken enhetskonverterare vill du använda?")
svar = input(" 1: C -> F, 2: C -> K, 3: F -> C, 4: F -> K, 5: K -> C, 6: K -> F?")

svar = int(svar)

if svar == 1:
    def celciustofarenhight(C):   
        F = (9/5) * C + 32
        return F
    a = float(input("skriv temperatur i celcius: ")) 
    print (celciustofarenhight(a))

elif svar == 2:
    def celciustokelvin(C):
        K = C + 273.15
        return K
    a = float(input("Skriv temperatur i celcius: "))
    print(celciustokelvin(a))

elif svar == 3:
    def farenhighttocelcius(F):
        C = (F - 32) / (9/5)

        #måste göra om alla dessa formler till korekt, den ovanför är korekt gjord matematiskt, men inte testad i kod.

        return C
    a = float(input("Skriv temperatur i farenhight: "))
    print (farenhighttocelcius(a))

elif svar == 4:
    def farenhighttokelvin(F):   
        K = ((5/9) * F -32) + 273.15
        return F
    a = float(input("skriv temperatur i farenhight: ")) 
    print (farenhighttokelvin(a))

elif svar == 5:
    def kelvintocelcius(K):
        C = K - 273.15
        return K
    a = float(input("Skriv temperatur i kelvin: "))
    print(kelvintocelcius(a))

else: 
    def kelvintofarenhight(K):
        F = ((9/5) * C + 32) - 273.15
        return C
    a = float(input("Skriv temperatur i kelvin: "))
    print (kelvintofarenhight(a))