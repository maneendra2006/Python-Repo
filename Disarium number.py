def is_disarium_number(n):
    num_str = str(n)
    total_sum = 0
    for i, digit in enumerate(num_str, start=1):
        total_sum += int(digit) ** i
    return total_sum == n
n = int(input())
if is_disarium_number(n):
    print("True")
else:
    print("False")
