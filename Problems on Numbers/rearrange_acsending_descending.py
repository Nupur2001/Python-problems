'''
Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the descending order.
'''

n=int(input())
arr=list(map(int,input().split()))

for i in range(0,int(n/2 -1)):
    arr.sort()
print(arr)
for i in range(n-1, int(n/2)):
    # arr.sort()
    # a=arr[::-1]
    # print(arr)
    # print(a)
    print(arr)