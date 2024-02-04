'''
Harshad/Niven Numbers
Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

Example 2:
Input: 379
Output: No
 it is not a Harshad number.
Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.
'''


t=int(input("Enter the number of test cases: "))
while t>0:

    n=int(input())
    temp=n
    sum=0
    while temp!=0:
        sum+=temp%10    # Extract and add the last digit
        temp=temp//10   # Remove the last digit
    print(f"The sum of given number: {sum}")
    if n%sum==0:
        print(f"{n} is a harshad number")
    else:
        print(f"{n} is not a harshad number")
    t=t-1



t=int(input("Enter the number of test cases: "))
while t>0:

    n=int(input())
    temp=n
    sum=0
    digits=[]
    while temp!=0:
        digit = temp % 10
        sum += digit
        digits.append(str(digit))  # Add digit as a string to the list
        temp = temp // 10
    print("+".join(digits) + f" = {sum}")
    if n%sum==0:
        print(f"{n} is a harshad number")
    else:
        print(f"{n} is not a harshad number")
    t=t-1


