n = int(input("Enter the size of the array: "))
arr = []

# Taking user input for each element of the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

e = int(input("Enter the element you want to search in arr: "))

if e in arr:
    print(f"Element {e} is present at index {arr.index(e)}")
else:
    print("Element is not present in the array")


n,m=map(int,input().split())

arr=list(map(int,input().split()))
found=False
for i in range(len(arr)):
    if arr[i] == m:
        print(i)
        found=True
        break
if not found:
        print("-1")


def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
     
n=int(input())
arr=list(map(int,input().split()))
target=int(input())

print(linear_search(arr,target))


