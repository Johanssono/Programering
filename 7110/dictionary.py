dict = {""}

svar = input("vill du översätta några ord åt mig? ja/nej: ")

while svar == "ja":

    key_1 = input("Skriv ett ord på valfritt språk: ")

    dict[key_1]
    key_2 = input("Skeiv samma ord på svenska (om förra ordet redan var på svenska, skriv på valfritt språk): ")
    dict[key_1] = key_2
    svar = input("vill du översätta fler ord åt mig? ja/nej: ")

