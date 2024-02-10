n = int(input("Enter the size of the array: "))
arr = []

# Taking user input for each element of the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

e = int(input("Enter the element you want to search in arr: "))

if e in arr:
    print(f"Element {e} is present at index {arr.index(e)}")
else:
    print("Element is not present in the array")
