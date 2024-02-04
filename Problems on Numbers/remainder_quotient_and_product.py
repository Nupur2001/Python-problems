'''
Let's find remiander and quotient
'''
dividend,divisor=map(int,input("Enter dividend and divisor: ").split())
if dividend==0 or divisor==0:
    try:
        raise ValueError("Not possible")
    except:
        print("Invalid input. Please enter non-zeroes values for divident and divisor")
else:
    print(f"Dividend={dividend} and Divisor={divisor} Remainder={dividend % divisor} Quotient={dividend / divisor}")





'''
Multiply Numbers
Let's practice multiplication a bit.
Write a program to take two integers x and y as input from the user, multiply those integers and print the product.
'''
a,b=map(float,input("Enter the value of a and b: ").split())
print(a*b)