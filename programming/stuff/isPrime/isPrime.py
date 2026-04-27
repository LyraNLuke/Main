

# Write any program you like!
# Use comments to explain what you did and why.

def isPrime(num):  #checks if a given number is prime (not most efficiant way)
    if num <= 1 : return False  #anything lower that 1 cant be prime
    checker = 2  #starts counting at 2
    while checker * 2 <= num:  #stops counting when checker > num/2 to avoid checking to large numbers
        curr = checker  #simplefies counting
        while curr + checker <= num:  #checks if num is devidable by by the current checker
            if curr + checker == num: return False  
            curr += checker 
        checker += 1  #goes trough each number lower than half of num
    return True  #if not proven fals then the given number is prime



def primeTill(num):  #gives a list of primes till a certain number
    primes = []
    i = 1  #forgot how to use the for function
    while i <= num:  #gose through each number to test for primes
        if isPrime(i): primes.append(i)  #add primes to list
        i+=1
    return primes  #returns prime list

print (primeTill(100))