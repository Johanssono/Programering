import time

text=input("Ange ett heltatl: ")
if text.isdigit():
    text=float(text)
    if text % 2==0:
        print('Grattis, du klarade av att följa enkla instruktioner')
    elif text % 2!=0:
        print('talet är lika udda som ditt utsende')
else:
    print("Nu var du allt rolig va?, eller kan du inte skillnaden mellan bokstäver och siffror."),
    time.sleep(5)
    print("...")
    time.sleep(10)
    print("Förutsattt nu inte var ett jävl extra och skrev in ett negativt tal, isåfall grattis, jag kan inte sånt än.")
print("Försvinn nu")
