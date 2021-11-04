import random
ronde = 1
#--Dobbelstenen--#
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0

#--Gebruikte punten--#
existingItems = ["Enen", "Tweën", "Drieën", "Vieren", "Vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]
unusedScore = existingItems

#--Bewaar dobbelstenen--#
keep1 = "N"
keep2 = "N"
keep3 = "N"
keep4 = "N"
keep5 = "N"

#--Punten Lijst 1--#
topListScore = {
    "Enen": 0,
    "Tweën": 0,
    "Drieën": 0,
    "Vieren": 0,
    "Vijven": 0,
    "Zessen": 0
}
topListTotal = 0

#Punten bovenste lijst#
Total1 = 0
bonus = 0

#--Punten Lijst 2--#
bottomListScore = {
    "ThreeOfAKind": 0,
    "FourOfAKind": 0,
    "FullHouse": 0,
    "SmallStraight": 0,
    "LargeStraight": 0,
    "Chance": 0,
    "Yahtzee": 0
}

#--EindScore--#
Totaal = 0

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

            global topListTotal
            topListTotal += score
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

            global topListTotal
            topListTotal += score
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
        if dobbel1 == 3:
            score += 3
        if dobbel2 == 3:
            score += 3
        if dobbel3 == 3:
            score += 3
        if dobbel4 == 3:
            score += 3
        if dobbel5 == 3:
            score += 3
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":

            global topListTotal
            topListTotal += score
            topListScore["Drieën"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def BerekenVieren():
    if topListScore["Vieren"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 4:
            score += 4
        if dobbel2 == 4:
            score += 4
        if dobbel3 == 4:
            score += 4
        if dobbel4 == 4:
            score += 4
        if dobbel5 == 4:
            score += 4
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":

            global topListTotal
            topListTotal += score
            topListScore["Vieren"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def BerekenVijven():
    if topListScore["Vijven"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 5:
            score += 5
        if dobbel2 == 5:
            score += 5
        if dobbel3 == 5:
            score += 5
        if dobbel4 == 5:
            score += 5
        if dobbel5 == 5:
            score += 5
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":

            global topListTotal
            topListTotal += score
            topListScore["Vijven"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def BerekenZessen():
    if topListScore["Zessen"] > 0:
        print("U heeft deze al gebruikt, Kies een andere.")
        WelkePunten()
    else:
        score = 0
        if dobbel1 == 6:
            score += 6
        if dobbel2 == 6:
            score += 6
        if dobbel3 == 6:
            score += 6
        if dobbel4 == 6:
            score += 6
        if dobbel5 == 6:
            score += 6
        Proceed = input("Weet U zeker dat U deze wil gebruiken voor " + str(score) + " punten?(Y/N): ").upper()
        if Proceed == "Y":

            global topListTotal
            topListTotal += score
            topListScore["Zessen"] += score
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def ThreeOfAKind():
    VerdientPunten = True
    check1 = dobbel1
    check2 = "None"
    if dobbel2 == dobbel1:
        amount1 = 2
    else:
        check2 = dobbel2
        amount2 = 1

    if dobbel3 == check1:
        amount1 += 1
    elif dobbel3 == check2:
        amount2 += 1
    else:
        if check2 == "None":
            check2 = dobbel3
        else:
            VerdientPunten = False

    if dobbel5 == check1:
        amount1 += 1
    elif dobbel3 == check2:
        amount2 += 1
    else:
        if check2 == "None":
            check2 = dobbel5
        else:
            VerdientPunten = False
    
        if dobbel4 == check1:
            amount1 += 1
        elif dobbel3 == check2:
            amount2 += 1
        else:
            if check2 == "None":
                check2 = dobbel4
            else:
                VerdientPunten = False

def WelkePunten():
    print("Waar wil je je punten voor gebruiken?")
    print(unusedScore)
    localLoop = "Yes"
    while localLoop == "Yes":
        print("Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)","Chance(13)","Yahtzee(14)")
        try:
            Gebruik = int(input("Typ hier: "))
            break
        except ValueError:
            print("Vul een nummer in")
    if Gebruik == 1 and "Enen" in unusedScore:
        unusedScore.remove("Enen")
        BerekenEnen()
    elif Gebruik == 2 and "Tweën" in unusedScore:
        unusedScore.remove("Tweën")
        BerekenTweën()
    elif Gebruik == 3 and "Drieën" in unusedScore:
        unusedScore.remove("Drieën")
        BerekenDrieën()
    elif Gebruik == 4 and "Vieren" in unusedScore:
        unusedScore.remove("Vieren")
        BerekenVieren()
    elif Gebruik == 5 and "Vijven" in unusedScore:
        unusedScore.remove("Vijven")
        BerekenVijven()
    elif Gebruik == 6 and "Zessen" in unusedScore:
        unusedScore.remove("Zessen")
        BerekenVijven()
    
    else:
        print("Kies een andere.")
        WelkePunten()



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
    print(topListScore)
