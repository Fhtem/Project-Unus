import random

init_deck = {}

for number in range(1, 14):
	for suit in ['spades', 'clubs', 'diamonds', 'hearts']:
		if number == 1:
			key = 'ace of %s' % (suit)
			deck[key] = 1
		elif number <= 10:
			key = '%d of %s' % (number, suit)
			deck[key] = number
		elif number == 11:
			key = 'jack of %s' % (suit)
			deck[key] = 10
		elif number == 12:
			key = 'queen of %s' % (suit)
			deck[key] = 10
		elif number == 13:
			key = 'king of %s' % (suit)
			deck[key] = 10
deck = init_deck

print (len(deck))
print (keys(deck))
