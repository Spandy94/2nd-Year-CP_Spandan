# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

# def handtodice(hand):
# 	# your code goes here
# 	hand = str(hand)
# 	# print(hand)
# 	hand = list(map(int, hand))
# 	hand = tuple(hand)

# 	return hand

def handtodice(hand):
	# your code goes here
	# hand = str(hand)
	li = []
	while(hand>0):
		li.append(hand%10)
		hand = hand//10
		
	return tuple(reversed(li))

