'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You hould not use the sum() or len () functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
Example Input 1
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output 1
total height = 857
number of
students = 5
average height = 171
'''
n=int(input())
height=list(map(int,input("Enter the height: \n").split()))
sum=0
if len(height)==n or len(height)<=n:
    for i in height:
        sum+=i
    print("Sum of all the elements is: ",sum)
    average=int(sum/n)
    print("Average of all the elements is: ",average)
else:
    print("Out of index")