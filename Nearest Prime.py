import bisect
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False 
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    primes = [i for i in range(limit + 1) if sieve[i]]
    return primes, sieve
def nearest_prime(N, primes, sieve):
    if sieve[N]:
        return N
    idx_up = bisect.bisect_left(primes, N)
    idx_down = idx_up - 1
    if idx_down < 0:
        return primes[idx_up]
    prime_down = primes[idx_down]
    prime_up = primes[idx_up] if idx_up < len(primes) else float('inf')
    
    if abs(prime_down - N) <= abs(prime_up - N):
        return prime_down
    else:
        return prime_up

limit = 10**6 + 1000
primes, sieve = sieve_of_eratosthenes(limit)

T = int(input())
for _ in range(T):
    N = int(input())
    print(nearest_prime(N, primes, sieve))
