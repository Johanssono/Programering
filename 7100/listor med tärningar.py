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
print (plats)
"""

# for tal in l: | är en for loop som går igenom varge tal i listan l.
# antal[tal] += 1 | skapar en lista vid namn "antal" och kollar så att varge nummer i listan "l" stämmer överäns med sin plats i listan. listan har indexen 0, 1, 2 osv upp till index 6. Om ett ett tal i listan "l" har värdet 4 så kommer listan "antal" att öka med 1 på index fyra. Så för varge 4 i listan "l" kommer index 4 på listan "antal" att öka med 1. På samma sätt kommer index 5 i listan "antal" att öka med 1 för varge 5,a i listan "l".



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

list = [antalettor, antaltvåor, antaltreor, antalfyror, antalfemmor, antalsexor]

print(list)
maximalt = max(list)
test = list.index(maximalt)
test = test + 1
print (test)