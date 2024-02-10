n=int(input())
arr=list(map(int,input().split()))
if len(arr)==n or len(arr)<=n:
  for i in range(n):
      if arr[i]%2==0:
          print(arr[i],"-> even")
      else:
          print(arr[i],"-> odd")
else:
   print("Out of index")




n=int(input())
arr=list(map(int,input().split()))
if len(arr)==n or len(arr)<=n:
  even=[]
  odd=[]

  for i in range(n):
    if arr[i]%2==0:
      even.append(arr[i])
    else:
      odd.append(arr[i])


  print(" ".join(map(str, even)))    
  print(" ".join(map(str, odd)))

else:
   print("Out of index")



