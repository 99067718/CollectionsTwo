from math import trunc
from os import truncate, waitpid
import os
import time
import sys
from time import sleep
import webbrowser
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

namenLijst = ["Jan-Peter","Lonald_Frump","Bustin_Jieber","Muper_Sario","GoldPilot2035","SuperAwesomeUsername","Rark-Mutte","Weerd_Gilders","Bhierry-Taudet","Bilfred Wouman","GateKeeper","DuckFuckMaster", "Karel", "Tante_Hendy", "Bertha", "Kees", "Henk", "Kim_jong-un", "Donald_Trump", "Obama", "Opa_Koos", "Ome_Gerda", "Jaap_klaas", "Zwarte_Piet", "xXCoolBoi69Xx", "Emiel", "Wilfred","Panneke_Veters", "Sinterklaas", "Jevil", "Sans", "Papyrus", "Peppa-Pig", "Piet-Jan","Duck", "PP_Master420","NoLife","UNO_reverse","Haha_UnoGoBrr","OriginalUsername","Username", "MinecraftPro", "KlokkenMeester","MarkRobbertYT","Mark_Zuckerberg","Pringles","PoopSwagMan", "PoopMasterLuke", "IAmSoSuperCool", "AnimeBoi", "MemeMan_Swag", "LuckyMan","Steve", "RobloxMan", "\_(•◡•)_/", "Luigi", "Waluigi", "Wario", "WAH"]

repeated = 0
kaart2 = ""

#Speler kaarten#
MainPlayerDeck = []
player2Deck = []
player3Deck = []
player4Deck = []
player5Deck = []
player6Deck = []
player7Deck = []
player8Deck = []
player9Deck = []
player10Deck = []

#Speler Score#
MainPlayerScore = 0
player2Score = 0
player3Score = 0
player4Score = 0
player5Score = 0
player6Score = 0
player7Score = 0
player8Score = 0
player9Score = 0
player10Score = 0

#Spelernamen#
player2Naam = random.choice(namenLijst)
namenLijst.remove(player2Naam)

player3Naam = random.choice(namenLijst)
namenLijst.remove(player3Naam)

player4Naam = random.choice(namenLijst)
namenLijst.remove(player4Naam)

player5Naam = random.choice(namenLijst)
namenLijst.remove(player5Naam)

player6Naam = random.choice(namenLijst)
namenLijst.remove(player6Naam)

player7Naam = random.choice(namenLijst)
namenLijst.remove(player7Naam)

player8Naam = random.choice(namenLijst)
namenLijst.remove(player8Naam)

player9Naam = random.choice(namenLijst)
namenLijst.remove(player9Naam)

player10Naam = random.choice(namenLijst)
namenLijst.remove(player10Naam)

KaartenLijst = {
"blauw" : 19, 
"groene": 19,
"rode": 19,
"gele": 19,
"neem-twee rood": 2,
"neem-twee geel": 2,
"neem-twee blauw": 2,
"neem-twee groen": 2,
"Uno reverse rood": 2,
"Uno reverse blauw": 2,
"Uno reverse groen": 2,
"Uno reverse geel": 2,
"Skip rood": 2,
"Skip geel": 2,
"Skip blauw": 2,
"Skip groen": 2,
"KeuzeKaart": 4,
"Neem-4": 4
}

def VerdeelKaarten(naam):
    print("Kaarten van", naam,"zijn aan het verdelen...")
    time.sleep(0.7)
    kaart2 = ""
    repeats = 0
    clearConsole()
    if naam == Username:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))

            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                MainPlayerDeck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player2Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player2Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player3Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player3Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player4Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player4Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player5Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player5Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player6Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player6Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player7Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player7Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player8Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player8Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player9Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " +nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player9Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break
    elif naam == player10Naam:
        while True:
            repeats += 1
            kaart = random.choice(list(KaartenLijst))
            
            #Checkt of de kaart een normale kaart is#
            if kaart == "blauw"or kaart == "rode" or kaart == "groene" or kaart == "gele":
                nummer = str(random.randint(0,9))
                kaart2 = kaart + " " + nummer
            else:
                kaart2 = kaart

            if KaartenLijst[kaart] > 0:
                KaartenLijst[kaart] -= 1
                player10Deck.append(kaart2)
            else:
                repeats -= 1
            if repeats == 7:
                break

while True:
    try:
        print()
        time.sleep(1)
        aantal = input("Met hoeveel mensen wilt U dit spelen: ")
        if aantal == "no":
            print("what do you mean 'no'?")
        aantal = int(aantal)
        if aantal <2:
            print("Dat zijn niet genoeg spelers...")
        elif aantal == 69:
            print("69 is een mooi getal, maar wel te veel.")
            webbrowser.open("https://media1.giphy.com/media/Bap9PFewF20es/giphy.gif")
        elif aantal == 49:
            print("De 4 en de 9 zijn de enige nummers in de rickroll link :)")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
        elif aantal == 66:
            print("Dit hoor jij helemaal niet te weten...")
            webbrowser.open("https://www.youtube.com/watch?v=bZgeoFO2rVA&ab_channel=RamseiGamer")
        elif aantal == 420:
            print("Nice, maar wel te veel.")
        elif aantal == 69420:
            print("I can do anything!!!")
            webbrowser.open("https://c.tenor.com/uxKOOSciM2YAAAAC/dancing-jevil-gif-dance.gif")
        elif aantal > 10:
            if repeated  == 1:
                words = "... "
                for char in words:
                    sleep(0.7)
                    sys.stdout.write(char)
                    sys.stdout.flush()
            elif repeated == 2:
                print("Meen je dit...")
            elif repeated == 3:
                print("Stop")
            elif repeated == 4:
                print("Ik zeg het nog één keer.")
                print("Dit spel heeft een maximum van 10 spelers.")
            elif repeated == 5:
                print("Je maakt een grapje zeker???")
            elif repeated == 6:
                print("STOP")
            elif repeated == 9:
                print("Ik ben er klaar mee...")
                time.sleep(2)
                print("IK BEN ER ZO ENORM KLAAR MEE!")
                time.sleep(2)
                print("WAAROM LUISTER JE NOOIT NAAR MIJ...")
                time.sleep(2)
                print("VIND MAAR EEN ANDER SPEL OM TE SPELEN...")
                time.sleep(2)
                words = "FJKSEHFISHFUSHFISJSIJEFAJIOFALFJAFJKENMKASNFNSFJNFJKSNAFKNAFKLDNJKLANSFJDNASLFNAJKFNDSFNSMNNXCVXCNMNKD"
                for char in words:
                    sleep(0.01)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                exit()
            elif repeated >= 7:
                words = "... "
                for char in words:
                    sleep(0.7)
                    sys.stdout.write(char)
                    sys.stdout.flush()
            else:
                print("Sorry maar dit spel heeft een maximum aantal spelers van 10.")
            repeated += 1
        else:
            print("Als je een random username wil type dan \"random\" ")
            Username = input("Vul een gebruikersnaam in: ")
            if Username == "random" or Username == "Random":
                Username = random.choice(namenLijst)
                break
            else:
                break
    except ValueError:
        print("Leuk dat je dit met", aantal,"wil spelen, maar dat is geen nummer....")
        time.sleep(2)
        print("Probeer het opnieuw")

clearConsole()
print("Hallo",Username,"vandaag speel je UNO tegen")
if aantal == 2:
    print(player2Naam)
elif aantal == 3:
    print(player2Naam+" en "+ player3Naam)
elif aantal == 4:
    print(player2Naam+", "+player3Naam+" en ", player4Naam)
elif aantal == 5:
    print(player2Naam+", "+player3Naam+", "+player4Naam+" en "+ player5Naam)
elif aantal == 6:
    print(player2Naam+", "+player3Naam+", ",player4Naam+", "+player5Naam+" en "+ player6Naam)
elif aantal == 7:
    print(player2Naam+", ",player3Naam+", "+player4Naam+", "+player5Naam+", "+player6Naam+" en "+ player7Naam)
elif aantal == 8:
    print(player2Naam+", "+player3Naam+", "+player4Naam+", "+player5Naam+", "+player6Naam+", "+player7Naam+" en "+ player8Naam)
elif aantal == 9:
    print(player2Naam+", "+player3Naam+", "+player4Naam+", "+player5Naam+", "+player6Naam+", "+player7Naam+", "+player8Naam+" en "+ player9Naam)
elif aantal == 10:
    print(player2Naam+", "+player3Naam+", "+player4Naam+", "+player5Naam+", "+player6Naam+", "+player7Naam+", "+player8Naam+", "+player9Naam+" en "+ player10Naam)

input("Druk op Enter om de kaarten te verdelen.")

def jeDeck():
    print("Jouw kaarten:",MainPlayerDeck)

for i in range(aantal):
        if i == 0:
            VerdeelKaarten(Username)
        elif i == 1:
            VerdeelKaarten(player2Naam)
        elif i == 2:
            VerdeelKaarten(player3Naam)
        elif i == 3:
            VerdeelKaarten(player4Naam)
        elif i == 4:
            VerdeelKaarten(player5Naam)
        elif i == 5:
            VerdeelKaarten(player6Naam)
        elif i == 6:
            VerdeelKaarten(player7Naam)
        elif i == 7:
            VerdeelKaarten(player8Naam)
        elif i == 8:
            VerdeelKaarten(player9Naam)
        elif i == 9:
            VerdeelKaarten(player10Naam)
        else:
            print("Ik weet niet hoe je dit hebt gedaan, maar je hebt het programma gesloopt...")
print("")
print("De kaarten zijn verdeeld.")

def PrintDecks():
    for i in range(aantal):
        if i == 0:
            print(Username,":",MainPlayerDeck)
        elif i == 1:
            print(player2Naam,":",player2Deck)
        elif i == 2:
            print(player3Naam,":",player3Deck)
        elif i == 3:
            print(player4Naam,":",player4Deck)
        elif i == 4:
            print(player5Naam,":",player5Deck)
        elif i == 5:
            print(player6Naam,":",player6Deck)
        elif i == 6:
            print(player7Naam,":",player7Deck)
        elif i == 7:
            print(player8Naam,":",player8Deck)
        elif i == 8:
            print(player9Naam,":",player9Deck)
        elif i == 9:
            print([player10Naam],":",player10Deck)

def JouBeurt():
    jeDeck()
    input("Welke wil je gebruiken?: ")

Showrules = input("Wil je dat ik wat dingetjes uitleg over hoe dit werkt? (Y/N): ").upper()
if Showrules == "Y":
    print("Maak functie die regels laat zien!!!")##############################Maak functie die regels laat zien!!!
jeDeck()