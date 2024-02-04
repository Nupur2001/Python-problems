def power_of_2(number):
    if number<=0:
        return False
    while number%2==0:
        number=number/2
    return number==1

input_number=int(input())
if power_of_2(input_number):
    print("The given number is a power of 2.")
else:
    print("The given number is not a power of 2.")