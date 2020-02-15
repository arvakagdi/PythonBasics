'''
Use Generator to get prime numbers
'''

def getPrimes():
    prime1 = 1
    primes = []
    while True:
        prime1 += 1
        for i in primes:
            if (prime1 % i == 0):
                break
        else:
            primes.append(prime1)
            yield(prime1)

primenumbers = getPrimes()

for i in range (20):
    print(primenumbers.__next__())
