'''
Last One
We all know computer understands only 0 and 1. Let's say you are given one such array A consisting only 0's and 1's. Your task is to print the last index of the 1 present in the array.

Input Format
The first line contains an integer T denoting the number of test cases.Each test case consists of two lines.
The first line contains N, number of elements in the array.
The second line contains N space-separated values either 0 or 1.

Output Format
For each test case on a new line, print index of the last 1 present in the array(0-based indexing). If no one is present in the array print -1.

Constraints
1<=T<=5

1<=N<=106

A[i]=0|1

Time limit
1 second

Example
Input
2

3
0 1 1

6
0 0 0 0 0 0
 

Output
2
-1
'''



t = int(input("Enter number of test cases: "))
while t > 0:
    n = int(input("Enter the number of elements: "))
    l = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        l.append(element)

    if 1 in l:
        print(len(l) - l[::-1].index(1) - 1)
    else:
        print('-1')

    t = t - 1



