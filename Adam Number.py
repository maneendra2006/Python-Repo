def is_adam_number(n):
    rev_num = int(str(n)[::-1])
    square_n = n * n
    square_rev_num = rev_num * rev_num
    if str(square_n)[::-1] == str(square_rev_num):
        return True
    return False
n = int(input())
if is_adam_number(n):
    print("True")
else:
    print("False")
