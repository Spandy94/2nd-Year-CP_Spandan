# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def isprime(n): #to check if the number is prime or not 
    if n == 2:
        return True
    elif n<2:
        return False
    elif n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i==0:
                return False
    return True

def sumofdigits(n): #list of digits
    nlist = [int(i) for i in str(n)]
    return sum(nlist)


def smithnumber(n): #checks if number is a smith number
    if(isprime(n)):
        return False
    elif(sumofdigits(n) == primefactors(n)):
        return True
    else:
        return False

def primefactors(n): #gives the list of prime factors
    # i = 1
    i = 2
    sum = 0
    l = []
    while i**2 <= n:
        if n % i == 0:
            sum += sumofdigits(i)
            l.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        l.append(n)
        sum += sumofdigits(n)
    return sum

def fun_nth_smithnumber(n):
    count = 0
    i = 1
    while (count <= n):
        if smithnumber(i):
            count += 1
            i+=1
        else:
            i+=1
    return i-1