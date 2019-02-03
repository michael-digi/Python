primes = []
prime_sum = 2
sieve = [True] * (2000000)
for i in range(3, 2000000,2):
    if (sieve[i]):
        prime_sum += i
        for j in range(i, 2000000, i):
            sieve[j] = False

print(prime_sum)