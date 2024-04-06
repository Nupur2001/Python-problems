sum=0
arr=list(map(int,input().split()))
arr=arr[::-1]
print(arr)
for i in arr:
    sum+=i
print(sum)




# # will ignore elements beyond the value of n
n = int(input())
sum=0
arr = list(map(int, input().split()))[:n]  
arr = arr[::-1]  
print(arr)

for i in arr:
    sum+=i
print(sum)



n = int(input("Enter the size of the array: "))
arr = []
sum=0

# Taking user input for each element of the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

    reversed_arr=arr[::-1]
    sum+=element

print(f'Reverse of array is: {reversed_arr}')
print(f'The sum of reversed array: {sum}')





