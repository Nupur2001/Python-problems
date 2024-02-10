'''
*
**
***
'''
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

'''
4 6
4
44
444
4444
44444
444444
'''
a,b=map(int,input().split())
for i in range(1,b+1):
    for j in range(i):
        print(a,end='')
    print()