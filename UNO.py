from os import waitpid
import time
import sys
from time import sleep
import webbrowser

KaartenLijst = {
"blauw" : 19, 
"groene": 19,
"rode": 19,
"gele": 19,
"neem-twee rood": 2,
"neem-twee geel": 2,
"neem-twee blauw": 2,
"neem-twee groen": 2,
"keer-om rood": 2,
"keer-om blauw": 2,
"keer-om groen": 2,
"keer-om geel": 2,
"Sla-beurt-over rood": 2,
"Sla-beurt-over geel": 2,
"Sla-beurt-over blauw": 2,
"Sla-beurt-over groen": 2,
"KeuzeKaart": 4,
"Neem-4": 4
}

while True:
    try:
        print()
        time.sleep(1)
        aantal = input("Met hoeveel mensen wilt U dit spelen: ")
        aantal = int(aantal)
        if aantal <2:
            print("Dat zijn niet genoeg spelers...")
        elif aantal >= 10000000:
            words = "... "
            for char in words:
                sleep(0.7)
                sys.stdout.write(char)
                sys.stdout.flush()
        elif aantal == 69:
            webbrowser.open("https://media1.giphy.com/media/Bap9PFewF20es/giphy.gif")
        elif aantal > 10:
            print("Sorry maar dit spel heeft een maximum aantal spelers van 10.")
        else:
            Username = input("Vul een gebruikersnaam in: ")
            break
    except ValueError:
        print("Leuk dat je dit met", aantal,"mensen wil spelen, maar dat is geen nummer....")
        time.sleep(2)
        print("Probeer het opnieuw")
        print()

print("Hallo",Username,"vandaag speel je UNO tegen",aantal-1,"bots success!!!")



