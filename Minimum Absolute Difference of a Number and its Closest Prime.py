import bisect
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    primes = [i for i in range(limit + 1) if sieve[i]]
    return primes, sieve
def min_prime_diff(N, primes, sieve):
    if sieve[N]:  
        return 0
    
    idx_up = bisect.bisect_left(primes, N)
    prime_up = primes[idx_up] if idx_up < len(primes) else float('inf')
    prime_down = primes[idx_up - 1] if idx_up > 0 else float('-inf')
    diff_up = abs(prime_up - N)
    diff_down = abs(prime_down - N)
    return min(diff_up, diff_down)

limit = 1000000
primes, sieve = sieve_of_eratosthenes(limit)

N = int(input())  
print(min_prime_diff(N, primes, sieve))  
