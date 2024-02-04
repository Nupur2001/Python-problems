n=int(input())
divisors=[]
sum=0
for i in range(1,n):
    if(n%i==0):
        divisors.append(str(i))
        sum+=i
# print(f"The sum of all proper divisors of {n} is {sum}")
if(sum==n):
    print(f"{n} has divisors {', '.join(divisors)}, and {' + '.join(divisors)} = {sum}, so {n} is a perfect number")
else:
    print(f"{n} has divisors {', '.join(divisors)}, and {' + '.join(divisors)} = {sum}, so {n} is not a perfect number")