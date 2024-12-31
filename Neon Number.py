def neon(n):
    s = n * n
    A = sum(int(d) for d in str(s))
    return A == n
N = int(input())
if neon(N):
    print("Neon Number")
else:
    print("Not Neon Number")
