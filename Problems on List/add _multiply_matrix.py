# def reverse():
# arr=list(map(int,input().split()))
n,m=map(int,input().split())
mat1=[]
for i in range(n):
    mat1.append(list(map(int,input().split())))


mat2=[]
for i in range(n):
    mat2.append(list(map(int,input().split())))
    
mat3=[]
for i in range(n):
    mat3.append([0]*m)
    
    
# Addition
for i in range(n):
    for j in range(m):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
for i in range(n):
    for j in range(m):
        print(mat3[i][j],end=' ')
    print()