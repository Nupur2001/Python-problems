n=int(input())
arr=[]
for i in range(n):
    element=int(input(f"Element{i+1}: "))
    arr.append(element)
print(arr)
# a=arr.remove(5)
a=arr.remove(n-1)
print(arr)
b=arr.append(6)
print(arr)
c=arr.insert(0,6)
print(arr)
    