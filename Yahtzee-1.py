from decimal import InvalidOperation
from os import truncate
import random
import time
from subprocess import check_call
ronde = 1
#Used Later#
amount1 = 0
amount2 = 0
aantalYahtzees = 0

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
bottomListTotal = 0
#--EindScore--#
Totaal = 0

def weetJeZeker(E = 0):
    print("Weet je zeker dat je deze wil gebruiken voor",E,"Punten?")

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

def Yahtzee():
    global bottomListTotal
    global aantalYahtzees

    CheckList = [dobbel1,dobbel2,dobbel3,dobbel4,dobbel5]
    x = CheckList.count(dobbel1)
    if x == 5 and aantalYahtzees == 0:
        bottomListTotal += 50
        bottomListScore["Yahtzee"] += 50
        unusedScore.remove("Yahtzee")
    elif x != 5:
        weetJeZeker(0)
        proceed = input("Y/N: ").upper()
        if proceed == "Y":
            print("U heeft zojuist uw kans op Yahtzee verspilt...")
        else:
            WelkePunten()
    

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
            unusedScore.remove("Enen")
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
            unusedScore.remove("Tweën")
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
            unusedScore.remove("Drieën")
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
            unusedScore.remove("Vieren")
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
            unusedScore.remove("Vijven")
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
            unusedScore.remove("Zessen")
        else:
            print("Welke wil je gebruiken?")
            WelkePunten()

def ThreeOfAKind():
    score = 0
    CheckList = [dobbel1, dobbel2, dobbel3, dobbel4, dobbel5]
    ones = CheckList.count(1)
    twos = CheckList.count(2)
    threes = CheckList.count(3)
    fours = CheckList.count(4)
    fives = CheckList.count(5)
    sixes = CheckList.count(6)
    
    if ones >= 3:
        score += ones
    elif twos >= 3:
        twos = twos * 2
        score += twos
    elif threes >= 3:
        threes = threes * 3
        score += threes
    elif fours >= 3:
        fours = fours * 4
        score += fours
    elif fives >= 3:
        fives = fives * 5
        score += fives
    elif sixes >= 3:
        sixes = sixes * 6
        score += sixes
    
    global bottomListTotal
    ###print("Weet je zeker dat je deze wil gebruiken voor",score,"Punten?")
    weetJeZeker(score)
    proceed = input("Y/N: ").upper()
    if proceed == "Y":
        unusedScore.remove("ThreeOfAKind")
        bottomListTotal += score
        bottomListScore["ThreeOfAKind"] += score

def FourOfAKind():
    score = 0
    CheckList = [dobbel1, dobbel2, dobbel3, dobbel4, dobbel5]
    ones = CheckList.count(1)
    twos = CheckList.count(2)
    threes = CheckList.count(3)
    fours = CheckList.count(4)
    fives = CheckList.count(5)
    sixes = CheckList.count(6)
    
    if ones >= 4:
        score += ones
    elif twos >= 4:
        twos = twos * 2
        score += twos
    elif threes >= 4:
        threes = threes * 3
        score += threes
    elif fours >= 4:
        fours = fours * 4
        score += fours
    elif fives >= 4:
        fives = fives * 5
        score += fives
    elif sixes >= 4:
        sixes = sixes * 6
        score += sixes
    
    global bottomListTotal
    ###print("Weet je zeker dat je deze wil gebruiken voor",score,"Punten?")
    weetJeZeker(score)
    proceed = input("Y/N: ").upper()
    if proceed == "Y":
        unusedScore.remove("FourOfAKind")
        bottomListTotal += score
        bottomListScore["FourOfAKind"] += score
    else:
        WelkePunten()

def FullHouse():
    global amount1
    global amount2
    amount1 = 1
    amount2 = 0
    check1 = dobbel1
    check2 = "None"
    if dobbel2 == check1:
        amount1 += 1
    else:
        amount2 = 1
        check2 = dobbel2

    if dobbel3 == check1:
        amount1 += 1
    elif dobbel3 == check2:
        amount2 += 1
    else:
        check2 = dobbel3
        amount2 = 1
    
    if dobbel4 == check1:
        amount1 += 1
    elif dobbel4 == check2:
        amount2 += 1
    else:
        check2 = dobbel4
        amount2 = 1

    if dobbel5 == check1:
        amount1 += 1
    elif dobbel5 == check2:
        amount2 += 1
    else:
        check2 = dobbel5
        amount2 = 1


    ##Checking score##
    global bottomListTotal
    if amount1 == 2 and amount2 == 3:
        ##print("Weet je zeker dat je dit wil gebruiken voor 25 punten?")
        weetJeZeker(25)
        antw = input("Y/N: ").upper()
        if antw == "Y":
            unusedScore.remove("FullHouse")
            bottomListTotal += 25
            bottomListScore["FullHouse"] += 25
            #x = unusedScore.count("kaas")
        else: 
            WelkePunten()
    elif amount2 == 2 and amount1 == 3:
        ##print("Weet je zeker dat je dit wil gebruiken voor 25 punten?")
        weetJeZeker(25)
        antw = input("Y/N: ").upper()
        if antw == "Y":
            unusedScore.remove("FullHouse")
            bottomListTotal += 25
            bottomListScore["FullHouse"] += 25
        else:
            WelkePunten()
    else:
        weetJeZeker(0)
        ###print("Weet je zeker dat je dit wil gebruiken voor 0 punten?")
        antw = input("Y/N: ").upper()
        if antw == "Y":
            unusedScore.remove("FullHouse")

def smallStraight():
    global bottomListTotal
    getScore = False
    CheckList = [dobbel1,dobbel2,dobbel3,dobbel4,dobbel5]
    if 1 in CheckList and 2 in CheckList and 3 in CheckList and 4 in CheckList:
        getScore = True
    elif 2 in CheckList and 3 in CheckList and 4 in CheckList and 5 in CheckList:
        getScore = True
    elif 3 in CheckList and 4 in CheckList and 5 in CheckList and 6 in CheckList:
        getScore = True
    if getScore == True:
        ###print("Weet je zeker dat je deze wil gebruiken voor 30 punten?")
        weetJeZeker(30)
        proceed = input("Y/N: ").upper()
        if proceed == "Y":
            bottomListTotal += 30
            bottomListScore["SmallStraight"] += 30
            unusedScore.remove("SmallStraight")
        else:
            WelkePunten()
    else:
        weetJeZeker(0)
        proceed = input("Y/N: ").upper()
        if proceed == "Y":
            bottomListTotal += 0
            bottomListScore["SmallStraight"] += 0
            unusedScore.remove("SmallStraight")
        else:
            WelkePunten()
        ###print("Weet je zeker dat je deze wil gebruiken voor 0 punten?")

def LargeStraight():
    global bottomListTotal
    getScore = False
    CheckList = [dobbel1,dobbel2,dobbel3,dobbel4,dobbel5]
    if 1 in CheckList and 2 in CheckList and 3 in CheckList and 4 in CheckList and 5 in CheckList:
        getScore = True
    elif 2 in CheckList and 3 in CheckList and 4 in CheckList and 5 in CheckList and 6 in CheckList:
        getScore = True
    if getScore == True:
        ###print("Weet je zeker dat je deze wil gebruiken voor 30 punten?")
        weetJeZeker(40)
        proceed = input("Y/N: ").upper()
        if proceed == "Y":
            bottomListTotal += 40
            bottomListScore["LargeStraight"] += 40
            unusedScore.remove("LargeStraight")
        else:
            WelkePunten()
    else:
        weetJeZeker(0)
        proceed = input("Y/N: ").upper()
        if proceed == "Y":
            bottomListTotal += 0
            bottomListScore["LargeStraight"] += 0
            unusedScore.remove("LargeStraight")
        else:
            WelkePunten()
        ###print("Weet je zeker dat je deze wil gebruiken voor 0 punten?")
    

def chance():
    global bottomListTotal
    total = dobbel1 + dobbel2 + dobbel3 + dobbel4 + dobbel5
    weetJeZeker(total)
    proceed = input("Y/N: ").upper()
    if proceed == "Y":
        bottomListTotal += total
        unusedScore.remove("Chance")
        bottomListScore["Chance"] += total
    else:
        WelkePunten()





def WelkePunten():
    print("Waar wil je je punten voor gebruiken?")
    print(unusedScore)
    localLoop = "Yes"
    while localLoop == "Yes":
        print("Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)","Chance(12)","Yahtzee(13)")
        try:
            Gebruik = int(input("Typ hier: "))
            break
        except ValueError:
            print("Vul een nummer in")
    if Gebruik == 1 and "Enen" in unusedScore:
        
        BerekenEnen()
    elif Gebruik == 2 and "Tweën" in unusedScore:
        
        BerekenTweën()
    elif Gebruik == 3 and "Drieën" in unusedScore:
        
        BerekenDrieën()
    elif Gebruik == 4 and "Vieren" in unusedScore:
        
        BerekenVieren()
    elif Gebruik == 5 and "Vijven" in unusedScore:
        
        BerekenVijven()
    elif Gebruik == 6 and "Zessen" in unusedScore:
        BerekenZessen()
    elif Gebruik == 7 and "ThreeOfAKind" in unusedScore:
        ThreeOfAKind()
    elif Gebruik == 8 and "FourOfAKind" in unusedScore:
        FourOfAKind()
    elif Gebruik == 9 and "FullHouse" in unusedScore:
        FullHouse()
    elif Gebruik == 10 and "SmallStraight" in unusedScore:
        smallStraight()
    elif Gebruik == 11 and "LargeStraight" in unusedScore:
        LargeStraight()
    elif Gebruik == 12 and "Chance" in unusedScore:
        chance()
    elif Gebruik == 13 and "Yahtzee" in unusedScore:
        Yahtzee()
    
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
    print(bottomListScore)

print("Ronde is voorbij, we zijn druk bezig met het berekenen van uw score...")
time.sleep(3)
if bottomListTotal >= 60:
    bonus = 35

FinalScore = bottomListTotal + bonus + topListTotal
print("Uw eindscore is:",FinalScore)
