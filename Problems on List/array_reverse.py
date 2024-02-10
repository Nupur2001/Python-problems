n=int(input())
arr=list(map(int,input().split()))

if len(arr)==n or len(arr)<=n:
       reverse_arr=arr[::-1]
       print(reverse_arr)
else:
      print("The length of the array should be equal to n.")