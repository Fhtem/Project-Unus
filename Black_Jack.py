import random

deck_values = {}

for number in range(1, 14):
	for suit in ['spades', 'clubs', 'diamonds', 'hearts']:
		if number == 1:
			key = 'ace of %s' % (suit)
			deck_values[key] = 1
		elif number <= 10:
			key = '%d of %s' % (number, suit)
			deck_values[key] = number
		elif number == 11:
			key = 'jack of %s' % (suit)
			deck_values[key] = 10
		elif number == 12:
			key = 'queen of %s' % (suit)
			deck_values[key] = 10
		elif number == 13:
			key = 'king of %s' % (suit)
			deck_values[key] = 10


def shuffle(deck, dct):
	deck = []
	for key in dct:
		deck.append(key)
	

def deal(deck, hand1, hand2):
	
	
