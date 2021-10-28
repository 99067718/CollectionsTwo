import random
ronde = 1
#--Dobbelstenen--#
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0

#--Gebruikte punten--#
existingItems = ["Enen", "Tweën", "Drieën", "Vieren", "vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]
unusedScore = existingItems

#--Bewaar dobbelstenen--#
keep1 = "N"
keep2 = "N"
keep3 = "N"
keep4 = "N"
keep5 = "N"

#--Punten Lijst 1--#
topListScore = {
    "Enen": int,
    "Tweën": int,
    "Drieën": int,
    "Vieren": int,
    "Vijven": int,
    "Zessen": int
}
topListTotal = int

#Punten bovenste lijst#
Total1 = int
bonus = int

#--Punten Lijst 2--#
bottomListScore = {
    "ThreeOfAKind": int,
    "FourOfAKind": int,
    "FullHouse": int,
    "SmallStraight": int,
    "LargeStraight": int,
    "Chance": int,
    "Yahtzee": int
}

#--EindScore--#
Totaal = int

def KeepItems():
    global keep1
    global keep2
    global keep3
    global keep4
    global keep5

    keep1 = input("Do you want to keep dobbelsteen 1? Y/N: ").upper()
    keep2 = input("Do you want to keep dobbelsteen 2? Y/N: ").upper()
    keep3 = input("Do you want to keep dobbelsteen 3? Y/N: ").upper()
    keep4 = input("Do you want to keep dobbelsteen 4? Y/N: ").upper()
    keep5 = input("Do you want to keep dobbelsteen 5? Y/N: ").upper()

def ControleDobbel(dobbel = int,steen = ""):
    if steen == "N":
        dobbel = random.randint(1,6)
        return dobbel
    return dobbel

def dobbelStenenGooien():
    global dobbel1
    global dobbel2
    global dobbel3
    global dobbel4
    global dobbel5

    input("Druk op Enter om de dobbelstenen te gooien.")
    dobbel1 = ControleDobbel(dobbel1, keep1)
    dobbel2 = ControleDobbel(dobbel2, keep2)
    dobbel3 = ControleDobbel(dobbel3, keep3)
    dobbel4 = ControleDobbel(dobbel4, keep4)
    dobbel5 = ControleDobbel(dobbel5, keep5)
    
    print("Dobbelsteen 1: " + str(dobbel1))
    print("Dobbelsteen 2: " + str(dobbel2))
    print("Dobbelsteen 3: " + str(dobbel3))
    print("Dobbelsteen 4: " + str(dobbel4))
    print("Dobbelsteen 5: " + str(dobbel5))

    KeepItems()

def BerekenEnen():
    if topListScore["Enen"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 1:
            score += 1
        if dobbel2 == 1:
            score += 1
        if dobbel3 == 1:
            score += 1
        if dobbel4 == 1:
            score += 1
        if dobbel5 == 1:
            score += 1
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":

            topListScore["Enen"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def BerekenTweën():
    if topListScore["Tweën"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 2:
            score += 2
        if dobbel2 == 2:
            score += 2
        if dobbel3 == 2:
            score += 2
        if dobbel4 == 2:
            score += 2
        if dobbel5 == 2:
            score += 2
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":
            topListScore["Tweën"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def BerekenDrieën():
    if topListScore["Drieën"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 2:
            score += 2
        if dobbel2 == 2:
            score += 2
        if dobbel3 == 2:
            score += 2
        if dobbel4 == 2:
            score += 2
        if dobbel5 == 2:
            score += 2
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":
            topListScore["Drieën"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def WelkePunten():
    print("Waar wil je je punten voor gebruiken?")
    print(unusedScore)
    print("Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)")
    Gebruik = input("Typ hier: ")


while ronde <= 13:
    keep1 = "N"
    keep2 = "N"
    keep3 = "N"
    keep4 = "N"
    keep5 = "N"

    ronde += 1
    for i in range(3):
        dobbelStenenGooien()
    WelkePunten()