n=input()
l=list(n)
sum=0
l.reverse()
for i in range(len(l)):
    sum=sum+int(l[i])*2**i
print(sum)
