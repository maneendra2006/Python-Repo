import math
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x
def is_fibonacci(n):
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return True
    return False
n = int(input())
print(is_fibonacci(n))
