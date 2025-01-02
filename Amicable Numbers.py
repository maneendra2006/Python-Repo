# Function to calculate the sum of proper divisors of a number
def sum_of_divisors(n):
    divisors_sum = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i: 
                divisors_sum += n // i
    return divisors_sum
def check_amicable(N, M):
    if sum_of_divisors(N) == M and sum_of_divisors(M) == N:
        return "Amicable"
    else:
        return "Not Amicable"
N = int(input())
M = int(input())
print(check_amicable(N, M))
