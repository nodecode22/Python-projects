# 1!+2!+3!.......n!
import math
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    x=math.factorial((i))
    sum=sum+x
print(f"the sum of series of factorial upto {n} terms is {sum}.")