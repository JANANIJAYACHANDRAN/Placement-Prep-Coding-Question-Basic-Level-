num= int(input("Enter a number:"))
total=0 
while num >0:
    rem= num%10
    total= total+rem 
    num =num//10
print("The sum of the given number is ",total)
