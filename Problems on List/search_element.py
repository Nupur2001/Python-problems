# Naive approach
n,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(n):
    if str(m)==str(arr[i]):
        print("Yes")
    else:
        print("No")



# Using break

n,m=map(int,input().split())
arr=list(map(int,input().split()))
found=False
for i in range(n):

    if m==arr[i]:
        found=True
        break
if found==True:
    print("Yes")
else:
    print("No")


# Another appraoch

n = int(input())
l = list(map(int, input().split()))
s = int(input("Enter an element you want to search: "))

if s in l:
    print("Element found at index of: ", l.index(s))
else:
    print("Element not found")

    