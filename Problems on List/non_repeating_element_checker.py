n=int(input())
arr=list(map(int,input().split()))
nrn=-1
for i in range(n):
    check=False
    for j in range(n):
        if i!=j and arr[i]==arr[j]:
            check=True
            break   
        
    if check==True:
        print(arr[i])
        break
    
if nrn!=-1:
    print(nrn)
else:
    print("All numbers are repeating")