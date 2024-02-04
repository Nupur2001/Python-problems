'''
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to X. IF X is 100 then the first even number would be 2 and the last one is 100:
Le. 2 + 4 + 6 + 8 4+10. + 98 + 100
Important, there should orty be 1 print statement in your comple output. & should just print the final total and not every step of the calculation.
Also, we wil constrain the inputs to only take numbers from 0 to a max of 1000
Example Input 1
10
Example Output 1
Example Input 2
52
Example Output 2
702
'''

# Using local varibales 
def even():
    sum_even=0
    i=1
    while i<=n:
        if i%2==0:
            # print(i)
            sum_even+=i
        i+=1
    print(f'The sum of even numbers is: {sum_even}')

def odd():
    sum_odd=0
    i=1
    while i<=n:
        if i%2!=0:
            # print(i)
            sum_odd+=i
        i+=1
    print(f'The sum of odd numbers is: {sum_odd}')

if __name__ == '__main__':
    n=int(input("Input\n"))
    even()
    odd()

