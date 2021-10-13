Lijstje = {}
AddMore = True
def NogIets():
    QuestionAnswered = False
    while QuestionAnswered == False:
        global AddMore
        nogIetsToevoegen = input("Wilt U nog wat toevoegen? (Y/N): ").upper()
        if nogIetsToevoegen == "N":
            AddMore = False
            break
        elif nogIetsToevoegen == "Y":
            AddMore = True
            break
        else:
            print("Dat begrijp ik niet, probeer het nog eens.")
            QuestionAnswered == False
    return AddMore

while AddMore == True:
    Toevoegen = input("Wat wil je aan je lijstje toevoegen?: ")
    Aantal = int(input("Hoeveel wilt U er hebben?: "))
    if Toevoegen in Lijstje:
        Lijstje[Toevoegen] = Lijstje[Toevoegen] + Aantal
    else:
        Lijstje[Toevoegen] = Aantal
    if NogIets() == False:
        break
    
print(Lijstje)