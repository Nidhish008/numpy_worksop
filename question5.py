#write a program to find if the given number is prime no or not

n=int(input("Enter the no:"))
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
if(count>=1):
    print("Not a prime no")
else:
    print("Prime no")

