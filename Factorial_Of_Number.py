num =int(input("Enter a number to find factorial:"))
def factorial(num):
    if num==0 or num==1:
        return 1 
    else:
        return num*factorial(num-1)
print(factorial(num))
