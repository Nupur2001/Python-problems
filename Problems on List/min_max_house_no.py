'''

Minimum house number
PrepBuddy lives in a colony, where 
N houses are built in a single row numbered from  0 to N-1 .The first house has a house number  0 , the second house has a house number  1  and so on, every house pays some rent at the end of the month. Help PrepBuddy in finding out the house number of the house paying the minimum rent.

Note: All house rents are unique.

Input format
First line contains test case T.
T test cases follow,
First line contains N representing the number of houses.
Second line contains the rent of the N houses.

Output format
For each test case on a new line, print house numbers(
0
- based indexing) that satisfy the above-mentioned condition.

Constraints
1<=T<=5

2<=N<=100

1<=A[i]<=1000

Time limit
1second

Example
Input
2

4 3 5 2 1

7
2 8 4 3 9 1

Output
4

6
'''


t=int(input())   # Test case
while t>0:
    n=int(input())  # Number of houses
    l=list(map(int,input().split()))
    min_rent=min(l)
    max_rent=max(l)
    min_rent_paying=l.index(min_rent)
    print(min_rent_paying)
    max_rent_paying=l.index(max_rent)
    print(max_rent_paying)
    t=t-1