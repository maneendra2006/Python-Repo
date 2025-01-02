def is_ugly_number(n):
    if n == 1:
        return "Ugly Number"
    for prime_factor in [2, 3, 5]:
        while n % prime_factor == 0:
            n //= prime_factor
    if n == 1:
        return "Ugly Number"
    else:
        return "Not Ugly Number"
n = int(input())
print(is_ugly_number(n))
