#PROGRAM TO FIND THE SUM OF SERIES GIVEN
x=int(input("enter the value of x:"))
a=int(input("enter the value of a:"))
n=int(input("enter the value of n sauak:"))
import math
sum=0
for i in range(1,n+1):
    f=math.factorial(i)
    if i%2==0:
        sum=sum+((x+a)**i/f)
    else:
        sum = sum - ((x + a) ** i / f)

print("sum=",sum)