import time

# Finding execution time but this is not a good approach
start=time.time()
L=[1,2,3,4,5]
# L=list(map(float,input().split()))
for i in L:
    for j in L:
        print('({},{})'.format(i,j))

print(time.time()-start)