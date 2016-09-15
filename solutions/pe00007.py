primes = [2,3,5,7,11]
primeCount = 5;
num = 12
limit = 10001

while primeCount < limit:
    prime = True
    for i in primes:
        if not (num % i):
            prime = False
            break
    if prime:
        primes.append(num)
        primeCount += 1
    else:
        num += 1

print primes[limit-1]
