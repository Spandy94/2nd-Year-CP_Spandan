# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 


def TP(n,k):
	if (n<k):
		return []
	
	elif (3**k <= n):
		return [3**k] + TP(n, k+1)
	else:
		return[]

def recursion_powersof3ton(n):
	# Your code goes here
	if (n <= 0):
		return None
	
	elif (0 < float(n) < 1): 
		return None

	else: 
		return TP(n, k = 0)
