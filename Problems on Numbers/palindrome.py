n=int(input())
temp=n
result=0
while n>0:
    remainder=n%10
    result=result*10+remainder
    n=n//10
if temp==result:
    print("Palindrome")
else:
    print("Not a palindrome")