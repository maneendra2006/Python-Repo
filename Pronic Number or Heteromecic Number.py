def is_pronic_number(X):
    n = 0
    while n * (n + 1) < X:
        n += 1
    if n * (n + 1) == X:
        return "YES"
    else:
        return "NO"
X = int(input())
print(is_pronic_number(X))
