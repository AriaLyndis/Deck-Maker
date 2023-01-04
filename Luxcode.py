import random

# Create deck
with open("LuxDeck.txt", "r") as deck:
	deck = deck.readlines()

# Remove newlines
for i in range(len(deck)):
	deck[i] = deck[i].replace("\n", "")

# Create empty hand
hand = []

# Create empty discard pile
discards = []

# Create play area
play_area = []

# Function Definitions
def shuffle(source):
	random.shuffle(source)

def draw(num = 1, source = deck, destination = hand):
	for i in range(num):
		# Add to destination the first card from the source
		destination.append(source.pop(0))

def keep_in_play():
	card = int(input("Which card?\n"))-1
	play_area.append(hand.pop(card))
	
def discard():
	card = int(input("Which card?\n"))-1
	discards.append(hand.pop(card))

def remove_from_play():
	card = int(input("Which card?\n"))-1
	discards.append(play_area.pop(card))

def print_cards(source):
	i = 1
	for card in source:
		print(str(i) + " " + card)
		i+=1

# Game Set Up
shuffle(deck)
draw(4)

# Game Loop
while True:
		print("________________________")
		print("_________HAND___________")
		print_cards(hand)
		print("________________________")
		print("_______PLAY AREA________")
		print_cards(play_area)
		print("________________________")
		print("________DISCARDS________")
		print_cards(discards)
		print("__________________________________________________________________________")
		print("______________________________CHOOSE ACTION_______________________________")
		move = input("1: Draw     2: Play/Discard      3: Put into play area      4: Remove From Play\n")

		if (move == "1"):
			draw()
		elif(move == "2"):
			discard()
		elif(move == "3"):
			keep_in_play()
		elif(move == "4"):
			remove_from_play()
		else:
			break