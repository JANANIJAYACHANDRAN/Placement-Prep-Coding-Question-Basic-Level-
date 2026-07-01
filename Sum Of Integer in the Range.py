print("The sum of integers in the given range")
start = int(input("Enter the starting value: "))
end= int(input("Enter the ending value: "))
sum=0
for i in range (start, end+1):
    sum+=i
print("The sum of integers in the given range is ", sum)
