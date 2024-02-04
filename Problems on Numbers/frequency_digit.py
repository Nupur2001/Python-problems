# t=int(input("Enter the number of test cases: "))
# while t>0:    

#     n = input()  
#     number_to_find = int(input())  

#     digit_list = list(map(int, n))  
#     frequency = digit_list.count(number_to_find)  

#     print(frequency)  

#     t -= 1 


t=int(input())
while(t>0):
  n=input()
  number_to_find=int(input())
  digit_list=list(map(int,n))
  frequency=digit_list.count(number_to_find)
  print(frequency)
  
  t=t-1