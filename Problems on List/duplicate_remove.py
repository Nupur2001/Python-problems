# Unsorted array
n=int(input())
arr=[]
for i in range(n):
    element=input(f"Enter element{i+1}: ")
    arr.append(element)
    s=set(arr)
print(s)


# Sorted array
n=int(input())
arr=[]
for i in range(n):
    element=input(f"Enter element{i+1}: ")
    arr.append(element)
    arr.sort()
    # print(arr)
    s=set(arr)
print(s)

