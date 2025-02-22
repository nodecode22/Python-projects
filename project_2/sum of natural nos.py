#program to fins the sum of natural number
n=int(input("enter the value of n: "))
sum=0
for i in range(1,n+1,1):
    sum+=i

print(f"The sum of natural number upto {n} is {sum}")
