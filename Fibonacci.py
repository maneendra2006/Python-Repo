def fibonacci(n):
    if n == 1:
        print(0)
        return
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print(" ".join(map(str, fib)))
n = int(input())
fibonacci(n)
