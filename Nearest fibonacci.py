def nearest_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib1, fib2 = 0, 1
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
    if abs(fib2 - n) < abs(fib1 - n):
        return fib2
    elif abs(fib2 - n) > abs(fib1 - n):
        return fib1
    else:
        return fib1, fib2
n = int(input())
result = nearest_fibonacci(n)
if isinstance(result, tuple):
    print(result[0], result[1]) 
else:
    print(result)
