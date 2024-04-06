# two list is pass as input to the program
# input
# [2,2,3,4,5,6,7]
# [2,8,9,5,0,1]
# output
# 2 5
#note:
# we have to check the number which is available in both list
# we have to consider that number one time

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=set(arr1)
arr4=set(arr2)
for i in arr1:
    for j in arr2:
        if i==j:
            print(i)
            found = True
            break
if not found:
    print("No repeating elements found")

