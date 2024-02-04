n,m=map(int,input().split())
sum=0
temp=n
while temp>0:
    remainder=temp%10
    sum+=remainder ** m
    temp=temp//10
if n==sum:
        print("Armstrong number")
else:
    print("Not an armstrong number")
