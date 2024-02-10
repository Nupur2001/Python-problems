def mode():
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    max_frequency = max(frequency_dict.values())
    mode_value = [key for key, value in frequency_dict.items() if value ==  max_frequency]

    if len(mode_value) == 1:
        print(f"Mode: {mode_value[0]}")
    else:
        print("No unique mode")

mode()
