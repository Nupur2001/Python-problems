n = int(input())
l = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    l.append(element)

sum_val = 0
for i in l:
    sum_val += i

print(f"Sum: {sum_val}")
average = sum_val / n
print(f"Average: {average}")

def check_sum():
    if sum_val % 2 == 0:
        print("Sum is even.")
    else:
        print("Sum is odd.")

def check_average():
    if average % 2 == 0:
        print("Average is even.")
    else:
        print("Average is odd.")

if __name__ == "__main__":
    check_sum()
    check_average()
