import math
lower = 2
upper = 331
primes = []
for x in range(lower,upper+1):
    factors = []
    for i in primes:
        if i >math.ceil(x/2):
            break
        if math.fmod(x,i) == 0:
            factors.append(i)
    print (x,factors)
    if factors == []:
        primes.append(x)            
                
print(primes) 
print ("There are ")
print(len(primes))
print("primes above.")

