import random
import math

## This program finds a large prime number


## Step 1:
## Pick random number between 1 to 10000
def pickRand():

    ## Set gcd flag to false
    gcdFlag = False

    ## Loop until gcd(n, 2310) = 1
    while (not gcdFlag):

        ## Generate a random int
        n = random.randint(1, 10000)

        ## Check if gcd of n and 2310 = 1
        if (math.gcd(n, 2310) == 1):
            gcdFlag = True
            
    ## Return the random integer such that gcd(n, 2310) = 1 
    return n        

## Print the random number
## print(pickRand())



## Step 2:
## Pick a random integer K such that x = 2310K +n is 100-bit long
def getPossiblePrime():

    ## get a random number between 1 to 10000
    n = pickRand()

    ## Generate k such that x will be 30 digit long
    k = random.randint(5.4876649e+26, 1.097533e+27)

    ## Determine x (possible prime)
    x = 2310 * k + n

    ## Return the possible prime number
    return x

## Print the possible prime
print (getPossiblePrime())
