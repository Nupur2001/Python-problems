# 4 4 4 4 
# 4 4 4 
# 4 4 
# 4 

n=int(input("Number: "))
for i in range(5,0,-1):
    for j in range(i):
        print(n,end=" ")
    print()


n,m=map(int,input().split())
for i in range(m,0,-1):
    for j in range(i):
        print(n,end=' ')
    print()