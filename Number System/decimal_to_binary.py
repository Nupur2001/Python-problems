n=int(input())
l=list()
while n>0:
    remainder=n%2
    l.append(remainder)
    n=n//2    # (Quotient)
l.reverse()
for element in l:
    print(element,end="")
# print(l)

