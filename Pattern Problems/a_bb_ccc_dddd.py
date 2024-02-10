n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        c=i
        print(chr(c+96),end='')
    print()