'''  a number whose sum of the factorials of its digits is equal to the original number itself'''
def check_strong(num):  
    #It's the definition of the function it gets the number as input 
    temp= num  # it stores the number in the temp 
    total_sum =0  # It will store the sum of the factorials of each digit 
    #process each digit from right to left 
    while temp>0 :
        digit = temp%10
        fact=1 
        for i in range(1, digit+1):
            fact*=i
        total_sum +=fact 
        temp=temp//10
    return total_sum ==num 
    
user_input= int(input("Please enter a number: "))
if check_strong(user_input):
    print("It's a strong number.")
else: 
    print("It's not a strong number.")
        
    
