from numpy import random
global userBet

userBet = int(input("Input credits: "))

while userBet > 0:
    roll = random.randint(1, 36)
    print("you have: ",userBet," credits")
    numBet = input("do you want to bet on a number? y/n: ")
    if numBet == "y":
        numBetBet = input("place bet: ")
        if int(numBetBet) > userBet:
            print("insufiscient funds")
            numBetBet = input("place bet: ")
        else:
            print(roll)
            numPBet = int(input("enter a number between 1 and 36: "))
            if numPBet == roll:
                userBet = userBet + (int(numBetBet) * 10)
                print("you won: ")
                print(userBet)
            else:
                print("you lost your bet")
    else:
        colorBet = input("do you want to bet on a color? y/n: ")
        if colorBet == "y":
            colorCreditBet = input("place bet: ")
            if int(colorCreditBet) > userBet:
                print("insufiscient funds")
                colorCreditBet = input("place bet: ")
            else: 
                print(roll)
                colorGuess = input("guess r/b: ")
                if colorGuess == "r" and roll % 2 == 0:
                    print("number is red")
                    print("you are right")
                    userBet = userBet + int(colorCreditBet)
                    print(userBet)
                elif roll % 2 != 0 and colorGuess == "r":
                    print("number is black")
                    print("you gussed " + colorGuess)
                    userBet = userBet - int(colorCreditBet)
                elif colorGuess == "b" and roll % 2 == 0:
                    print("number is red")
                    print("you guesed " + colorGuess)
                    userBet = userBet - int(colorCreditBet)
                elif colorGuess == "b" and roll % 2 != 0:
                    print("number is black")
                    print("your right")
                    userBet = userBet + int(colorCreditBet)
                    print(userBet)