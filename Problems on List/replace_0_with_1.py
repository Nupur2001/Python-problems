n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i]==0:
        print("1",end=' ')
    else:
        print(arr[i],end=' ')