# Example:
# Input: N = 5, array[] = {1,2,3,4,5}
# insertbeginning(6)
# insertending(7)
# insertatpos(8,4)
# Output: 6,1,2,8,3,4,5,7
# Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4 

n = int(input("Enter the size of the array: "))
arr = []

# Taking user input for each element of the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
print(arr)


def insertbeginning():
    x = int(input())
    arr.insert(0, x)
    print("Insert at the beginning:\n",arr)

def insertending():
    y = int(input())
    arr.append(y)
    print("Insert at the ending:\n",arr)

def insert_at_position():
    pos, num = map(int, input().split())
    arr.insert(pos, num)
    print("Insert at the position:\n",arr)

insertbeginning()
insertending()
insert_at_position()
