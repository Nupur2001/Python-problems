n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n):
    for j in range(0,i):
        if arr[i]==arr[j]:
            print(arr[i])
            break