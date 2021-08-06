# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def isHappyNumber(n):
    if n<=0:
        return False
    else:
        count = 0
        while n>1:
            nlist = [int(i) for i in str(n)]
            n=0
            for i in nlist:
                n += i**2
                count += 1
                if count == 100:
                    return False
        return True

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def ishappyprimenumber(n):
    # Your code goes here
    if(isHappyNumber(n) == True):    
        if(isPrime(n) == True):
            return True
    return False

# def ishappyprimenumber(n):
#     # Your code goes here
#     # pass
#     if isprime(n)==True:
#         if isHappyNumber(n)==True:
#             return True
#         else:
#             return False
#     else:
#         return False
