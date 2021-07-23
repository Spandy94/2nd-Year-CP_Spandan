# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def factorslist(l):
	flist = []
	for i in range(1, l+1):
		if l%i == 0:
			flist.append(i)
	return flist

def isPrime(l):
	for i in range(2,int(l**0.5)+1):
		if l%i == 0:
			return False
	return True

def isPowerful(l):
	flist = factorslist(l)
	# print('factlist: ', flist)
	for i in flist:
		if isPrime(i) == True:
			# print('i and i**2',i,i**2)
			if i**2 not in flist:
				# print('i**2 not in factlist')
				return False
	# print('i**2 in factlist')
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	num = 1
	count = 0
	while count < n+1:
		# print('number= ', num)
		if isPowerful(num) == True:
			count += 1
			num -= 1
		else:
			num += 1
	return num-1
