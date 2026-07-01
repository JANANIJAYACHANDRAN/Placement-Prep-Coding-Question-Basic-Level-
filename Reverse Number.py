num =int(input("Enter the number to reverse: "))
rev=0 
while num >0:
    digit = num %10
    rev=(rev*10)+digit
    num//=10
print(rev)
# This is only positive integer with trailing zeroes 
