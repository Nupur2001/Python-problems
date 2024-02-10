# Print all the duplicate charachters


n=input()
arr={}
for i in n:
    if i in arr:
        arr[i]+=1
    else:
        arr[i]=1
for i,freq in arr.items():
    if freq>1:
        print(i,"-",freq)
        