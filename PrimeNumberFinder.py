import math
import random

#miller_rabin method shows if we have a possible prime 'n' for the given 'a'
def miller_rabin(x, a):
    

    #if n is even, then, we know it's not a prime
    if(x%2 == 0):
        #print(x, " is not a prime since it is even.")
        return False

    #we're getting the odd value for q from the equation: x-1 = (2^s)q. We're also getting the value of s which is the highest power of 2 which satisfies this equation.
    s = 0
    q = x - 1
    while q & 1 == 0:        
        q >>= 1          #division by 2
        q = int(q)
        s += 1
    

    #if (a^q) mod x is 1, then there is a possibility that a is a prime
    if pow(a, q, x ) == 1:
        #print(x, " is possibly a prime.")
        return True         #this returns True i.e. this number could be a prime
        
    i = 0

    #looping through the range for s = 0 to s-1 (Step 5 of the algorithm)
    while i < s:
        #if (a^q) mod x is -1, then there is a possibility that a is a prime
        if pow(a, q, x) == -1:
            #print(x, " is possibly a prime.")
            return True

        #if (a^q) mod x isn't -1, then we will check for (a^2q) mod x until we get to s
        q <<= 1                #multiplication  by 2 
        i+= 1
    #print(n, " is a composite.")
    return False

#this method calls the miller_rabin method but for different values of a to ensure that we are not getting any strong liars
def different_a_test(n):
    flag = False
    while flag == False:
        a = random.randint(2, n-1)          #picking a random integer "a" between 1 and n-1 
        if (miller_rabin(n, a) == False):
            return False
        else:
            flag = True
            return True

    
#this method picks a random value for n for the equation x = 2310K + n where gcd(n, x) = 1
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

#variable to store the number of times we had to try different values for K to get a possible prime
count = 0;
possiblePrime = 0;

#this method calculates the value of x from the n calculated from above, and then calls the different_a_test(x) method to check if it;s a prime.
def check_prime(n):
    global count
    global possiblePrime
    found = False
    listK = []
    a = (math.pow(2,100) - 9999)/2310
    b = (math.pow(2,101) - 1)/2310

    #while we don't have a prime, we take a different value of k and then add that value to the list, we will get a new value of x which will be checked for
    #different value of a as well
    while not found:
        count += 1
        k = random.randint(a, b)
        listK.append(k)
        x = 2310*n + k
        if(different_a_test(x)):
            found = True            #the loop stops executing after we get a prime
    possiblePrime = x
    print(x, " is possibly a prime number we got after trying ", len(listK), " tries for K.") 
    print (listK)
    return listK

n = pickRand()
KList  = check_prime(n)
print(len(KList), " tries for K were required to get a possible prime number ", possiblePrime)
print(count)
