import random
#import pickle

#Game variables
cardColourList = ["red", "green", "yellow"]
deck = 15
playagain = ("y")

#Player score variables
playerScore1 = 0
playerScore2 = 0

def cards():
    while playagain == ("y") or playagain == ("Y"):
        #card 1 variables
        cardNumber = random.randint(1,10)
        cardColourSelector = random.randint(0,2)

        #card 2 variables
        card2Number = random.randint(1,10)
        card2ColourSelector = random.randint(0,2)

        #variable applier
        card2 = cardColourList[card2ColourSelector]
        card1 = cardColourList[cardColourSelector]

        #tell the players the result
        print("Player 1's card is %s %i" %(card1, cardNumber))
        print("Player 2's card is %s %i" %(card2, card2Number))
        compare()
        print("Player %i won" %win)

        if win == 1:
            playerScore1 += 1
            deck -= 1

        else:
            playerScore2 += 1
            deck -= 1


def compare():
    if cardColourSelector == card2ColourSelector:
        if cardNumber > card2Number:
            win = 1
        else:
            win = 2

    else:
        if cardColourSelector == 0 and card2ColourSelector == 1:
            win = 1

        elif cardColourSelector == 1 and card2ColourSelector == 2:
            win = 1

        elif cardColourSelector == 2 and card2ColourSelector == 0:
            win = 1

        else:
            win = 2

cards()


    
