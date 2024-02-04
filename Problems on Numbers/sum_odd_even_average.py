n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
average=sum/n
print(average)
if sum%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
if average%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
