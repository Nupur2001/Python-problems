# V pattern

# t=int(input())
# while(t>0):
#     ch=input()
#     n,spaces=map(int,input().split())
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end='')
#         for k in range(1,spaces+1):
#             print(end=' ')
#         spaces-=2
#         for j in range(i,0,-1):
#             print(j,end='')
#         print()
#         t=t-1



# # dry run
ch=input()
spaces=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(1,spaces):
        print(end=' ')
    spaces=spaces-2
    for j in range(i,0,-1):
        print(j,end='')
    print()