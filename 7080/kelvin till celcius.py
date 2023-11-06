def kelvin(F):   
    C = (5/9) * (F - 32)
    return C

a = float(input("skriv temperatur i celcius ")) 
print (kelvin(a))