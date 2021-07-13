# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here



# def getKthDigit(digit, k):
# 	#5123//10**2
# 	#51 % 10

# 	#5123//10**3
# 	#5 % 10

# 	digit = abs(digit)
# 	p = digit//(10**k)
# 	v = p % 10
# 	return v