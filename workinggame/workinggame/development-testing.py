import random

#lists & variables
player1list = []
player2list = []
colours = ["r", "g", "y"]
numbers = []

for counter in range (1,11):
    numbers.append(counter)

for colour in range(len(colours)):
    for number in range(len(numbers)):
        card = colours [ colour ] + str ( numbers [ number ] )
        cards.append(card)

deck = []
