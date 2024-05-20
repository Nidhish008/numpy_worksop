# find if the given number is a palindrome or not?

n=int(input("Enter the number:"))
n1=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(n1==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
