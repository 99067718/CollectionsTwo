import random
existingCards = ["Klaver", "Harten", "Schoppen", "Ruiten", "joker"]
soorten = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
Deck = []
jokers = 2
for i in range(47):
    cardColor = random.choice(existingCards)
    cardNumber = random.choice(soorten)
    if cardColor == "joker" and jokers > 0:
        jokers -= 1
        Deck.append(cardColor)
    elif cardColor == "joker" and jokers == 0:
        i -=1
    else:
        add = cardColor,cardNumber
        Deck.append(add)
print(Deck)

