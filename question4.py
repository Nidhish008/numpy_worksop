#write a program to find the sum of digits of a given number

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

n=int(input("Enter the number:"))     
print("The sum of digits is ",sum_of_digits(n))