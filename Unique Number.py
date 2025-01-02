def check_unique_number(n):
    num_str = str(n)
    seen_digits = set()
    for digit in num_str:
        if digit in seen_digits:
            return "Not Unique Number"
        seen_digits.add(digit)
    return "Unique Number"
n = int(input())
print(check_unique_number(n))
