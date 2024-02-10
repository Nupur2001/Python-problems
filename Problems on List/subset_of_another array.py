# # By converting list/array into set
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

set1=set(arr1)
set2=set(arr2)

if set1.issubset(set2):
    print(f'{set1} is a subset of {set2}')
else:
    print(f'{set1} is not a subset of {set2}')


# by not converting list/arr into set

# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# is_subset=True
# for i in arr1:
#     if i not in arr2:
#         is_subset=False
#         break
# if is_subset:
#     print(f'{arr1} is a subset of {arr2}')
# else:
#     print(f'{arr1} is not a subset of {arr2}')