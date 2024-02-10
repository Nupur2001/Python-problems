# # Write a python code to count how many prime integers are there in a given list of integers.
# For example, if you want to give a list of 4 integers with values 3,5,7,11
# then in the text area for customized input, provide the input as follows:
# 4
# 3
# 5
# 7
# 11
# Where first line represents the number of elements in the input list ie 4

# Output:
# For the above example, the output will be:
# 4


n=int(input())
nums=list(map(int,input().split()))
count=0


def is_prime(num):
    # for n in nums:
        if num<=1:
            return False

        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
        

for num in nums:
    if is_prime(num):
        count+=1
print(count)
if count==0:
    print("No prime number found")
