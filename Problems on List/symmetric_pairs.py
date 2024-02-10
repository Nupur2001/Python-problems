n = int(input())  # Take user input for the size of the array
arr = []  # Initialize an empty list to store the pairs

# Take user input for the pairs as a string
arr_input = input()

# Parse and convert input string to a list of pairs
arr_items = arr_input.split()
for item in arr_items:
    pair = tuple(item.strip("()").split(","))
    # pair = tuple(map(int, item.strip("()").split(",")))
    arr.append(pair)

# Iterate through the pairs and find symmetric pairs
for i in range(n):
    for j in range(i + 1, n):
        if arr[j][0] == arr[i][1] and arr[j][1] == arr[i][0]:
            print("Symmetric Pair:", arr[i])
            break

