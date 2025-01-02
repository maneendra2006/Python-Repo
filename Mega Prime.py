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

def is_mega_prime(n):
    if not is_prime(n):
        return "Not Mega Prime"
    prime_digits = {'2', '3', '5', '7'} 
    for digit in str(n):
        if digit not in prime_digits:
            return "Not Mega Prime"
    
    return "Mega Prime"

N = int(input())  
print(is_mega_prime(N)) 
