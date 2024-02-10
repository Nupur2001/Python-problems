t=int(input())
while t>0:
    n=int(input())
    l=list(map(int,input().split()))
    product=1
    for i in l:
        product*=i
    print(product)
    t=t-1