def median():
    n = int(input())
    arr = []

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    if n % 2 == 0:
        median_value = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median_value = sorted_arr[n // 2]

    print(f"Median = {median_value}")

median()
