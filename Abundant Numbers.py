import math
def is_abundant_number(n):
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i  
            if i != 1 and i != n // i:  
                divisor_sum += n // i
    return divisor_sum > n
n = int(input())
if is_abundant_number(n):
    print("True")
else:
    print("False")
