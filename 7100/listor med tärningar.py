import random

a = 10

l = []

while a > 0:
    b = random.randrange(1, 7)

    l.append(b)

    a = a - 1

print(l)

l.sort ()

print(l)

print("summa: ", sum(l))

medel = sum(l) / len(l)

print("medel: ", medel)

print("minsta: ", min(l))

print("största: ", max(l))

antalsexor = 0
for tal in l:
    if (tal == 6):
        antalsexor = antalsexor + 1
print("Antal sexor: ", antalsexor)

antal = [0, 0, 0, 0, 0, 0, 0] # antal 0, antal 1, antal 2, ...


"""
for tal in l:
    antal[tal] += 1
print(antal)

maximum = max(antal)
plats = antal.index(maximum) 
"""

# Ska försöka få den att räkna det vanligaste värdet på ett enklare sätt, 


antalfyror = 0
antalfemmor = 0
for tal in l:
    if (tal == 5):
       antalfemmor  = antalfemmor + 1 

    if (tal == 4):
        antalfyror = antalfyror + 1 
         
antaltreor= 0
for tal in l:
    if (tal == 3):
        antaltreor = antaltreor + 1 
    
antaltvåor = 0
for tal in l:
    if (tal == 2):
        antaltvåor = antaltvåor + 1 
        
antalettor= 0
for tal in l:
    if (tal == 1):
        antalettor = antalettor + 1

list = [antalsexor, antalfemmor, antalfyror, antaltreor, antaltvåor, antalettor]

print("vanligaste talet: ", max(list))
