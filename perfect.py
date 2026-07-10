num= int(input("Enter a number to check if perfect or not: "))
def is_perfect_simple(n):
    if n <= 1:
        return False
    
    divisor_sum = 0
    # No proper divisor can be larger than half of the number
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisor_sum += i
            
    return divisor_sum == n
if(is_perfect_simple(num)):
    print("It's Perfect.")
else: 
    print("Not a perfect number.")
