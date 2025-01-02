import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_pair(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
           
            if is_prime(i) and is_prime(N // i) and i != N // i:
                return (i, N // i)
    return -1

N = int(input())  
result = find_prime_pair(N)

if result == -1:
    print(result)
else:
    print(result[0], result[1])
