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
Hint
There are quite a few ways of solving this problem, but you wil need to use the range () function in any of the solutions.
'''

def even(start_even,end_even):
    sum_even=0
    for i in range(start_even,end_even+1):
        if i%2==0:
            sum_even+=i
    return sum_even
def odd(start_odd,end_odd):
    sum_odd=0
    for i in range(start_odd,end_odd+1):
        if i%2==0:
            sum_odd+=i
    return sum_odd
    




if __name__=="__main__":
    start_range_even=int(input())
    end_range_even=int(input())

    result_even=even(start_range_even,end_range_even)
    print(f'The sum of even numbers from {start_range_even} to {end_range_even} is: {result_even}')


    start_range_odd=int(input())
    end_range_odd=int(input())

    result_odd=even(start_range_odd,end_range_odd)
    print(f'The sum of even numbers from {start_range_odd} to {end_range_odd} is: {result_odd}')
    # even()
