from math import trunc
import random
upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
specialCharacters = ["@", "#", "$", "%", "&", "_", "?"]

smallCharacters = 0
CapitalLetters = 0
AmountOfNumbers = 0
amountOfCharacters = 0
password = []

def NoBrackets(list1):
    return str(list1).replace('[','').replace(']','').replace(",",'').replace("'",'').replace(" ",'')

def chooseLetter():
    global CapitalLetters
    global smallCharacters
    Check = random.randint(1,2)
    if Check == 1 and CapitalLetters <6:
        chosen = random.choice(upperCaseLetters)
        CapitalLetters += 1
    else:
        chosen = random.choice(lowerCaseLetters)
        smallCharacters += 1
    password.append(chosen)

def chooseNumber():
    global AmountOfNumbers
    if AmountOfNumbers < 7:
        chosen = random.choice(numbers)
        AmountOfNumbers += 1
    else:
        chosen = random.choice(lowerCaseLetters)
    password.append(chosen)

def specialCharacter():
    global amountOfCharacters
    if amountOfCharacters < 3:
        chosen = random.choice(specialCharacters)
        password.append(chosen)
        amountOfCharacters += 1

    else:
        chooseLetter()

e = True
while e == True:
    chooseLetter()
    for i in range(2):
        Check = random.randint(1,2)
        if Check == 1:
            chooseLetter()
        else:
            specialCharacter()

    for i in range(20):
        Check = random.randint(1,4)
        if Check == 1:
            chooseLetter()
        elif Check == 2:
            specialCharacter()
        else:
            chooseNumber()


    Check = random.randint(1,2)
    if Check == 1:
        chooseLetter()
    else:
        chooseNumber()
    if AmountOfNumbers < 4 and amountOfSpecialCharacters > 3:
        password
        password = []
    else:
        print("Password has been generated.")
        break
print(NoBrackets(password))