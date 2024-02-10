n=int(input())
arr=list(map(int,input().split()))
if len(arr)==n or len(arr)<=n:
    l=sorted(arr)
    print("Sorted list is:", l)
    l1=l[::-1]
    print("List in decending order:", l1)
else:
    print("Out of index")

