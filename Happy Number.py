def sum_of_squares(n):
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy_number(n):
    seen = set() 
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1  
n = int(input())
if is_happy_number(n):
    print("True")
else:
    print("False")
