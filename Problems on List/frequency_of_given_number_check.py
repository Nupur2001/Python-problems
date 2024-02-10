n,m=map(int,input().split())
arr=[]
for i in range(n):
    element=int(input(f"Enter Element{i+1}: "))
    arr.append(element)
    frequency=arr.count(int(m))
print(frequency)
