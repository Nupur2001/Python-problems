t=int(input())
while(t>0):
  n,m=map(int,input().split())
  if str(m) in str(n):
      print(f'{m} is in {n}')
  else:
      print(f'{m} is not in {n}')
      
  t=t-1
  

# # Dry run
# t=int(input())
# while(t>0):
#   n=int(input())
#   if '5' in str(n):
#       print(f'5 is in {n}')
#   else:
#       print(f'5 is not in {n}')
      
#   t=t-1