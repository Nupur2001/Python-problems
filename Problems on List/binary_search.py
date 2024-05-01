# For binary search list should always be sorted
# Time Complexity: log(n)


def binary_search(Arr,target):
    left,right=0,len(Arr)-1
    while left<=right:
        mid=(left+right)//2
        if Arr[mid]==target:
            return mid
        elif Arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

Arr=list(map(int,input().split()))
target=int(input())

print(binary_search(Arr,target))