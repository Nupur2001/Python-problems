n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        c=i
        k=i
        print(chr(c+64)+chr(k+96),end='')
        # print(chr(k+96),end='')
    print()



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        c=i
        k=i
        print(chr(c+64),end='')
        print(chr(k+96),end='')
    print()