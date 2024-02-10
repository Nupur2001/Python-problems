# Method 1 
arr=[]
for ele in input().split():
    arr.append(int(ele))
for i in range(len(arr)):
    print(arr[i],end=' ')


# Method 2
arr1=[]
arr1=list(map(int,input().split()))
for i in range(len(arr1)):
    print(arr1[i],end=' ')