def celciustofarenhight(C):   
    F = (9/5) * C + 32
    return F

def celciustokelvin(C):
    K = C + 273.15
    return K

def farenhighttocelcius(F):
    C = (F - 32) / (9/5)
    return C

def farenhighttokelvin(F):   
    K = ((F - 32) / (9/5)) + 273.15
    return K

def kelvintocelcius(K):
    C = K - 273.15
    return C

def kelvintofarenhight(K):
    F = ((K - 273.15) * (9/5)) + 32
    return F
print ("Hej, vilken enhetskonverterare vill du använda?")
svar = input(" 1: C -> F, 2: C -> K, 3: F -> C, 4: F -> K, 5: K -> C, 6: K -> F?")

svar = int(svar)

if svar == 1:
    temp = float(input("skriv temperatur i celcius: ")) 
    print (celciustofarenhight(temp))

elif svar == 2:

    temp = float(input("Skriv temperatur i celcius: "))
    print(celciustokelvin(temp))

elif svar == 3:

    temp = float(input("Skriv temperatur i farenhight: "))
    print (farenhighttocelcius(temp))

elif svar == 4:

    temp = float(input("skriv temperatur i farenhight: ")) 
    print (farenhighttokelvin(temp))

elif svar == 5:
    temp = float(input("Skriv temperatur i kelvin: "))
    print(kelvintocelcius(temp))

else: 

    temp = float(input("Skriv temperatur i kelvin: "))
    print (kelvintofarenhight(temp))