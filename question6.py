#write a program to find the maximum of two numbers
def max(a,b):
    if a>b:
        return a
    else:
        return b

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print(max(n1,n2))