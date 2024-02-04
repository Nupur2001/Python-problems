def Reverse():
  n=int(input())
  result=0
  while n:
    remainder=n%10
    n=n//10
    result=result*10+remainder
  return result
print(Reverse())

# def reverse():
#   x=int(input())
#   result=0
#   while(x>0):
#     result=result*10+x%10
#     x=x//10
#   return result
# print(reverse())