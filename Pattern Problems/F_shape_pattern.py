n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==0 or i==1 or j==0 or j==1):
            print("*",end=" ")
        else:
            print("",end=" ")
    print() 
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==0 or i==1 or j==0 or j==1):
            print("*",end=" ")
        else:
            print("",end=" ")
    print() 