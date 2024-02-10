n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Mean
def mean():
    sum = 0
    for i in arr:
        sum += i
    print(f"Mean = {sum / len(arr)}")

# Median
def median():
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        median_value = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median_value = sorted_arr[n // 2]
    print(f"Median = {median_value}")

# Mode
def mode():
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    max_frequency = max(frequency_dict.values())
    mode_value = [key for key, value in frequency_dict.items() if value == max_frequency]

    if len(mode_value) == 1:
        print(f"Mode: {mode_value[0]}")
    else:
        print("No unique mode")

mean()
median()
mode()
