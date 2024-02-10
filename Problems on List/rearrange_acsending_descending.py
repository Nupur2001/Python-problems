'''
Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the descending order.
'''

# n=int(input())
# arr=list(map(int,input().split()))

# arr[:int(n/2)]=sorted(arr[:int(n/2)])

# arr[int(n/2):]=sorted(arr[int(n/2):],reverse=True)

# arr[int(n/2):]=arr[int(n/2):][::-1]

# print(arr)

n = int(input())
arr = list(map(int, input().split()))

# Sort the first half in ascending and second half in descending order
arr[:int(n/2)] = sorted(arr[:int(n/2)])
arr[int(n/2):] = sorted(arr[int(n/2):], reverse=True)

# Instead of reversing, rearrange the second half elements directly:
temp = arr[:int(n/2)]
for i in range(int(n/2), n):
    arr[i] = temp.pop()

print(arr)
