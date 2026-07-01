a= int(input("Enter the no 1: "))
b=int(input("Enter the no 2: "))
def cal_lcm(a,b):
    greater =max(a,b)
    while True:
        if (greater%a==0) and (greater%b==0):
            lcm=greater 
            break
        greater +=1
    return lcm

print("The lcm is ",cal_lcm(a,b))
