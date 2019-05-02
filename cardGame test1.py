import random
import shelve

#Game variables
cardColourList = ["red", "green", "yellow"]
deck = 15
playagain = ("y")

#Player score variables
playerScore1 = 0
playerScore2 = 0
cardno1 = 0
cardno2 = 0

name = str(input("What is Player 1's name? "))
name2 = str(input("What is Player 2's name? "))

score = shelve.open('score.txt')

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
    print("%s's card is %s %i" %(name, card1, cardNumber))
    print("%s's card is %s %i" %(name2, card2, card2Number))

    cardno1 = cardno1 + 1
    cardno2 = cardno2 + 1

    #player1dict["Card", cardno1] = ("%s %i" %(card1, cardNumber))
    #player2dict["Card", cardno1] = ("%s %i" %(card2, card2Number))

    #comparison
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

    print("Player %i won" %win)

    if win == 1:
        playerScore1 += 1
        deck -= 1
        playagain = input("Do you want to play again? [y/n]\n>")

    else:
        playerScore2 += 1
        deck -= 1
        playagain = input("Do you want to play again? [y/n]\n>")

    if deck == 0:
        playagain = ("n")

        if playerScore1 > playerScore2:
            playerScore1 *= 2
            playerScore2 *= 2
            print("The winner is %s\n%s had %i cards" %(name, name, playerScore1))
            print("%s had %i cards" %(name2, playerScore2))

        else:
            playerScore2 *= 2
            playerScore1 *= 2
            print("The winner is %s \n %s had %i cards" %(name2, name2, playerScore2))
            print("%s had %i cards" %(name, playerScore1))

score['score'] = playerScore1
