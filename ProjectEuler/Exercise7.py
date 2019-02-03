def find_prime(n):
    primes = []
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if (sieve[i]):
            primes.append(i)
            for j in range(i, n+1, i):
                sieve[j] = False
    return primes[10000]

result = find_prime(200000)
print(result)