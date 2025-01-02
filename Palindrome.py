def is_palindrome(n):
    original = str(n)
    if original == original[::-1]:
        return True
    return False
n = int(input())
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
