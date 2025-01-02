import math
def is_perfect_square(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return True
    else:
        return False
n = int(input())
print(is_perfect_square(n))
