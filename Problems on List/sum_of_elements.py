n = int(input("Enter the size of the array: "))
arr = []
sum=0

# Taking user input for each element of the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
    arr.sort()
    sum+=element
print("Sum of array: ",sum)


