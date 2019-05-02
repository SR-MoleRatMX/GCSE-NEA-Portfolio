#modules
import random

#variables
playagain = ("y")

#variable for number to add to numbers list
add = 0

#a list containing all of the possible colours of the cards
colours = ["r", "g", "y"]

#a list containing all of the possible numbers of the cards
numbers = []

#list containing all of player 1's cards
player1cards = []

#list containing all of player 2's cards
player2cards = []

for i in range (10):
    #variable 'add' is increased by 1
    add += 1

    #variable 'add' is added to the list 'numbers'
    numbers.append(add)
    
#a list containing all possible values of the card e.g. r1, r2, r3 etc.
cards=[]

for colour in range(len(colours)):
    for number in range(len(numbers)):
        #takes the value in the 'colour'position in the colours list e.g. 1=g
        #and adds t to the number in the number position in the numbers list
        #e.g. 5 to create a value such as r1, r2, r3
        card = colours[colour]+str(numbers[number])

        #adds the 'card' variable to the 'cards' list
        cards.append(card)

#shuffles the cards
random.shuffle(cards)

name1 = str ( input ( "What is player 1's name?\n>" ) )
name2 = str ( input ( "What is player 2's name?\n>" ) )

while playagain == ("y") or playagain == ("Y"):
    #selects the top cards and then deletes them
    user1card = cards[len(cards)-1]
    cards.pop()
    user2card = cards[len(cards)-1]
    cards.pop()

    #dev code for checking the deck size

    #print( "-----" )
    #print("The deck has %s cards left" len ( cards ) )
    #print( "-----" )

    
    #splits the cards into the colour and number
    card1colour = user1card[0]#takes the first digit, the colour
    card1number = user1card[1]#takes the second digit, the number
    #print ( card1number )#dev code to check the digits
    #print ( card1colour )
    card2colour = user2card[0]
    card2number = user2card[1]
    #print ( card2number )
    #print ( card2colour )

    #checks if the cards colours are the same
    if card1colour == card2colour:
        #if they are the same, checks if player 1's cardis bigger than player 2's card
        if card1number > card2number:
            #if card 1 is bigger, adds both cards to player 1s deck
            print("Player 1 wins")
            player1cards.append( user1card )
            player1cards.append( user2card )
            #just checking the lists
            print("Player 1 has", player1cards )
            print("Player 2 has", player2cards )
            
        else:
            #and vice versa
            print("Player 2 wins")
            player2cards.append( user1card )
            player2cards.append( user2card )
            print("Player 1 has", player1cards )
            print("Player 2 has", player2cards )

    #if the cards have different colours
    else:
        #checking all possible card sets that provide a Player 1 win
        if card1colour == ("r") and card2colour == ("g") or card1colour == ("g") and card2colour == ("y") or card1colour == ("y") and card2colour == ("r"):
            print("Player 1 wins")

            #adds both cards to player 1s deck
            player1cards.append( user1card )
            player1cards.append( user2card )

            #prints the cards of each player
            print("Player 1 has", player1cards )
            print("Player 2 has", player2cards )

        else:
            #and vice versa
            print("Player 2 wins")
            player2cards.append( user1card )
            player2cards.append( user2card )
            print("Player 1 has", player1cards )
            print("Player 2 has", player2cards )

    if len(cards) == 0:
        playagain = ("n")
        print("")
        print("---------------")
        print("It's the end of the game.")
        print("Player 1 has", player1cards)
        print("Player 2 has", player2cards)

        if len(player1cards) > len(player2cards):
            player1cards.append( name1 )
            winninglist = player1cards
            print("Player 1 wins the game with %i cards" %len(player1cards)-1)
            print("Player 2 had %i less than Player 1 with %i cards" %(len(player1cards) - len(player2cards), len(player2cards-1)))
            print("To see if you got a high score, just run comparison.py")

        else:
            player2cards.append( name2 )
            winninglist = player2cards
            print("Player 2 wins the game with %i cards" %len(player2cards))
            print("Player 1 had %i less than Player 2 with %i cards" %(len(player2cards)-1 - len(player1cards)-1, len(player1cards)-1))
            print("To see if you got a high score, just run comparison.py")

    else:
        #asks the players if they want to do another round
        playagain = input("Do you want to play again? \n>")
