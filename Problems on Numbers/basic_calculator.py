a,b=map(float,input("Enter 2 numbers: \n").split())
operator=input("Enter an operator for calculating: ")
if operator=="+":
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
else:
    print("Please enter valid operator")