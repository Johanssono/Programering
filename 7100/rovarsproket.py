konsonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

svar = input("Skriv någonting!: ")

rovar_svar =""

for i in svar:
    if i in (konsonant):
        i = i + "o" + i
        rovar_svar = rovar_svar + i

print(rovar_svar)

#vill sakap en kod som kollar om en bokstav är en kosonant genom att kolla om bokstaven finns i "konsonant", om bokstaven är en konsonant, läggs bokstaven in i rövarformat in i variablen "rövar_svar"