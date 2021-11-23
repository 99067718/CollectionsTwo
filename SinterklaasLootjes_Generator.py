import math
import time
import random
namenLijst = []
ongebruikteNamen = []
getrokkenLootje = {}
HasGivenAmount = False

while HasGivenAmount == False:
    try:
        aantal = int(input("Met hoeveel mensen doet U dit?: "))
        if aantal <= 2:
            print("U moet op zijn minst met zijn drieën zijn om lootjes te trekken, vul wat anders in.")
        else:
            HasGivenAmount = True
    except ValueError:
        print("Probeer het opnieuw")
def Namen():
    for i in range(aantal):
        naam = input("naam "+str(i + 1)+": ")
        if naam in namenLijst:
            print("Deze naam staat al in de lijst, weet U zeker dat U deze in de lijst wil toevoegen?")
            while True:
                proceed = input("Y/N: ").upper()
                if proceed == "Y":
                    namenLijst.append(naam)
                    break
                elif proceed == "N":
                    print("Vul een nieuwe naam in.")
                    naam = input("naam "+str(i + 1)+": ")
                    namenLijst.append(naam)
                    #getrokkenLootje[naam] = ""
                    break
                else:
                    print("Sorry dat begreep ik niet.")
        else:        
            namenLijst.append(naam)
            #getrokkenLootje[naam] = ""

def randomLootje():
    print("Lootjes zijn aan het verdelen...")
    for i in range(0,aantal):
        chosen = random.choice(ongebruikteNamen)
        persoon = namenLijst[i]
        ongebruikteNamen.remove(chosen)
        getrokkenLootje[persoon] = chosen



Namen()

while True:
    print("Weet U zeker dat deze lijst klopt?")
    time.sleep(1)
    print(namenLijst)
    correct = input("Y/N: ").upper()
    if correct == "Y":
        break
    elif correct == "N":
        namenLijst = []
        getrokkenLootje = {}
        Namen()
    else:
        print("Sorry dat begreep ik niet.")

ongebruikteNamen = list(namenLijst)
randomLootje()
number = 0
i = 0
while True:
    persoon = list(getrokkenLootje.values()) [i]
    key = getrokkenLootje[persoon]
    i += 1
    if key == persoon:
        ongebruikteNamen = list(namenLijst)
        randomLootje()
        i = 0
    elif i == aantal:
        break

print(getrokkenLootje)






