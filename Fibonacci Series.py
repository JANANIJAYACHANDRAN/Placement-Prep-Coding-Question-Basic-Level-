x= int(input("Enter number of terms:"))
n1,n2=0,1
count=0
if x<=0:
    print("Enter a positive number")
elif x==1:
    print(n1)
else:
    print("Fibonacci Sequence:")
    while count<x:
        print(n1)
        nth= n1+n2
        n1=n2
        n2=nth 
        count +=1
